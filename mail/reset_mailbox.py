import os

USERS = ["alice", "bob"]

for user in USERS:
    maildir = f"/home/{user}/Maildir"

    for folder in ["new", "cur"]:
        path = os.path.join(maildir, folder)

        if os.path.exists(path):
            for f in os.listdir(path):
                try:
                    os.remove(os.path.join(path, f))
                except Exception as e:
                    print(f"Error deleting {f}: {e}")

print("Mailbox reset complete.")