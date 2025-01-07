# EKT
Cloud internship

Task 1

As this task was focused on Docker-Compose and SQL Database backup & restore,  I have made the simple FastAPI website. 

-Added log rotation 10 MB each up to 5. then auto-overwrite first.

-Added replica, restart policy on failure, failure rollback

-Created an auto database backup.

-For data restore from local machine to container 
docker cp E:/STUDY/EKT/backup/task.db.backup_2025-01-06_08-21-58.db task1:/app/task.db
