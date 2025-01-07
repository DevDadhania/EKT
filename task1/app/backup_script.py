import os
import time
import shutil
from datetime import datetime

# Path to the task.db in the container
db_source = "/app/task.db"

# Backup directory (mapped to your local Windows path)
backup_dir = "E:/STUDY/EKT/backup"

# Create the backup directory if it doesn't exist
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

def backup_db():
    # Create a timestamp for the backup file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = os.path.join(backup_dir, f"task_backup_{timestamp}.db")

    # Copy the database file to the backup directory with timestamp
    shutil.copy(db_source, backup_file)
    print(f"Backup created at {backup_file}")

if __name__ == "__main__":
    while True:
        backup_db()
        time.sleep(10)  # Wait for 10 seconds before creating the next backup
