import json
import re
from typing import Any, Dict

def safe_parse_json(text: str) -> Dict[str, Any]:
    """
    Try to parse LLM output as JSON.
    If it contains extra text, attempt to extract the JSON object.
    Always returns a dict with either valid fields or an error payload.
    """
    if not text:
        return {"ok": False, "error": "Empty LLM output", "raw": text}

    # 1) direct JSON parse
    try:
        data = json.loads(text)
        return {"ok": True, "data": data, "raw": text}
    except Exception:
        pass

    # 2) to extract the first {...} block
    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if match:
        candidate = match.group(0)
        candidate = re.sub(r",\s*([}\]])", r"\1", candidate)
        try:
            data = json.loads(candidate)
            return {"ok": True, "data": data, "raw": text}
        except Exception:
            return {"ok": False, "error": "Found JSON-like block but failed to parse", "raw": text}

    return {"ok": False, "error": "No JSON object found in output", "raw": text}

def normalize_flags(flags) -> list:
    """
    Ensure flags is ALWAYS a list of strings like ["F1", "F3"].

    Handles these bad outputs:
    - flags = [{"id":"F1"}, {"flag":"F3"}]
    - flags = "F1"
    - flags = [{"code":"F1", "reason":"..."}]
    """
    if flags is None:
        return []

    # If model returns one string instead of list
    if isinstance(flags, str):
        f = flags.strip()
        return [f] if f else []

    # If it's a list, clean each item
    if isinstance(flags, list):
        cleaned = []
        for item in flags:
            if isinstance(item, str):
                s = item.strip()
                if s:
                    cleaned.append(s)
            elif isinstance(item, dict):
                # common keys the model might output
                for key in ["id", "flag", "flag_id", "code", "name"]:
                    val = item.get(key)
                    if isinstance(val, str) and val.strip():
                        cleaned.append(val.strip())
                        break
        return cleaned

    # Unknown type
    return []

def normalize_result(parsed: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize the output into a stable schema your Flask UI can rely on.
    """
    if not parsed.get("ok"):
        return {
            "is_phishing": None,
            "phishing_type": "",
            "flags": [],
            "confidence": 0.0,
            "explanation": parsed.get("error", "Unknown error"),
            "raw_output": parsed.get("raw", "")
        }

    d = parsed["data"] if isinstance(parsed["data"], dict) else {}

    return {
        "is_phishing": d.get("is_phishing", None),
        "phishing_type": d.get("phishing_type", "") or "",
        "flags": normalize_flags(d.get("flags", [])),
        "confidence": float(d.get("confidence", 0.0) or 0.0),
        "explanation": d.get("explanation", "") or "",
        "raw_output": parsed.get("raw", "")
    }
