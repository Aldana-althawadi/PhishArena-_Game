import csv
import os
from datetime import datetime

LOG_FILE = "logs/game_results.csv"


def log_game_result(student_id, email_id, expected_label, student_answer, ai_answer, difficulty):
    # Check if the same record already exists
    if os.path.isfile(LOG_FILE):
        with open(LOG_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if (
                    row["student_id"] == str(student_id)
                    and row["email_id"] == str(email_id)
                    and row["student_answer"] == str(student_answer)
                ):
                    # Duplicate found → do not log again
                    return

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.stat(LOG_FILE).st_size == 0:
            writer.writerow([
                "timestamp",
                "student_id",
                "email_id",
                "expected_label",
                "student_answer",
                "ai_answer",
                "difficulty"
            ])

        writer.writerow([
            datetime.now().isoformat(),
            student_id,
            email_id,
            expected_label,
            student_answer,
            ai_answer,
            difficulty
        ])