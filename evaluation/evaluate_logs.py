import os
import pandas as pd

LOG_PATH = os.path.join("logs", "events.csv")
OUT_DIR = "reports"

def to_bool(x):
    """Convert common string/bool values to True/False/None safely."""
    if pd.isna(x):
        return None
    if isinstance(x, bool):
        return x
    s = str(x).strip().lower()
    if s in ["true", "1", "yes"]:
        return True
    if s in ["false", "0", "no"]:
        return False
    return None

def split_flags(s):
    """Split 'F1;F2;F3' into a set(['F1','F2','F3'])."""
    if s is None or pd.isna(s):
        return set()
    s = str(s).strip()
    if not s:
        return set()
    return set([f.strip() for f in s.split(";") if f.strip()])

def jaccard(a, b):
    """Jaccard similarity between two sets."""
    if not a and not b:
        return 1.0
    union = a | b
    if not union:
        return 1.0
    return len(a & b) / len(union)

def confusion_counts(y_true, y_pred):
    """Return TP, FP, TN, FN for phishing detection."""
    TP = ((y_true == True) & (y_pred == True)).sum()
    FP = ((y_true == False) & (y_pred == True)).sum()
    TN = ((y_true == False) & (y_pred == False)).sum()
    FN = ((y_true == True) & (y_pred == False)).sum()
    return TP, FP, TN, FN

def safe_div(a, b):
    return float(a) / float(b) if b else 0.0

def main():
    if not os.path.isfile(LOG_PATH):
        raise FileNotFoundError(f"Log file not found: {LOG_PATH}")

    os.makedirs(OUT_DIR, exist_ok=True)

    df = pd.read_csv(LOG_PATH)

    # Normalize phishing columns
    df["expected_is_phishing"] = df["expected_is_phishing"].apply(to_bool)
    df["model_is_phishing"] = df["model_is_phishing"].apply(to_bool)

    # Drop rows where we can't interpret expected/model
    df_clean = df.dropna(subset=["expected_is_phishing", "model_is_phishing"]).copy()

    # Confusion + basic metrics
    TP, FP, TN, FN = confusion_counts(df_clean["expected_is_phishing"], df_clean["model_is_phishing"])

    accuracy = safe_div(TP + TN, TP + TN + FP + FN)
    precision = safe_div(TP, TP + FP)
    recall = safe_div(TP, TP + FN)
    f1 = safe_div(2 * precision * recall, precision + recall)

    summary = pd.DataFrame([{
        "records_total": len(df),
        "records_used": len(df_clean),
        "TP": TP, "FP": FP, "TN": TN, "FN": FN,
        "accuracy": round(accuracy, 4),
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4)
    }])

    # Confusion matrix table
    confusion = pd.DataFrame(
        [
            {"expected": "phishing", "predicted_phishing": TP, "predicted_legit": FN},
            {"expected": "legit", "predicted_phishing": FP, "predicted_legit": TN},
        ]
    )

    # Flag similarity (Jaccard) per email
    df_clean["expected_flag_set"] = df_clean["expected_flags"].apply(split_flags)
    df_clean["model_flag_set"] = df_clean["model_flags"].apply(split_flags)
    df_clean["flag_jaccard"] = df_clean.apply(lambda r: jaccard(r["expected_flag_set"], r["model_flag_set"]), axis=1)

    flag_score = pd.DataFrame([{
        "avg_flag_jaccard": round(df_clean["flag_jaccard"].mean(), 4),
        "median_flag_jaccard": round(df_clean["flag_jaccard"].median(), 4)
    }])

    # Per-flag performance: treat each flag as a binary classification
    all_flags = sorted(set().union(*df_clean["expected_flag_set"]).union(*df_clean["model_flag_set"]))

    per_flag_rows = []
    for flag in all_flags:
        y_true = df_clean["expected_flag_set"].apply(lambda s: flag in s)
        y_pred = df_clean["model_flag_set"].apply(lambda s: flag in s)

        TPf = ((y_true == True) & (y_pred == True)).sum()
        FPf = ((y_true == False) & (y_pred == True)).sum()
        TNf = ((y_true == False) & (y_pred == False)).sum()
        FNf = ((y_true == True) & (y_pred == False)).sum()

        p = safe_div(TPf, TPf + FPf)
        r = safe_div(TPf, TPf + FNf)
        f = safe_div(2 * p * r, p + r)

        per_flag_rows.append({
            "flag": flag,
            "TP": TPf, "FP": FPf, "TN": TNf, "FN": FNf,
            "precision": round(p, 4),
            "recall": round(r, 4),
            "f1": round(f, 4)
        })

    per_flag = pd.DataFrame(per_flag_rows).sort_values(by="f1", ascending=False)

    # Per-type accuracy (optional, if you logged expected_type/model_type)
    per_type = None
    if "expected_type" in df_clean.columns and "model_type" in df_clean.columns:
        df_clean["type_match"] = df_clean["expected_type"].fillna("").astype(str).str.strip().str.lower() == \
                                 df_clean["model_type"].fillna("").astype(str).str.strip().str.lower()
        per_type = df_clean.groupby("expected_type", dropna=False).agg(
            count=("email_id", "count"),
            type_accuracy=("type_match", "mean")
        ).reset_index()
        per_type["type_accuracy"] = per_type["type_accuracy"].round(4)

    # Save outputs
    summary.to_csv(os.path.join(OUT_DIR, "summary_metrics.csv"), index=False)
    confusion.to_csv(os.path.join(OUT_DIR, "confusion_matrix.csv"), index=False)
    flag_score.to_csv(os.path.join(OUT_DIR, "flag_similarity.csv"), index=False)
    per_flag.to_csv(os.path.join(OUT_DIR, "per_flag_metrics.csv"), index=False)
    df_clean[[
        "ts", "email_id",
        "expected_is_phishing", "model_is_phishing",
        "expected_flags", "model_flags",
        "flag_jaccard", "confidence"
    ]].to_csv(os.path.join(OUT_DIR, "per_email_results.csv"), index=False)

    if per_type is not None:
        per_type.to_csv(os.path.join(OUT_DIR, "per_type_accuracy.csv"), index=False)

    # Print quick console summary
    print("=== Summary Metrics ===")
    print(summary.to_string(index=False))
    print("\n=== Confusion Matrix ===")
    print(confusion.to_string(index=False))
    print("\n=== Flag Similarity ===")
    print(flag_score.to_string(index=False))
    print("\nSaved reports to:", OUT_DIR)

if __name__ == "__main__":
    main()
