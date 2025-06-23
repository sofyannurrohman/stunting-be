import os
from fastapi import APIRouter
import subprocess

router = APIRouter()

@router.post("/import-sql")
def import_sql():
    db_url = os.getenv("DATABASE_URL")  # Example: mysql://user:pass@host:port/db
    if not db_url:
        return {"error": "DATABASE_URL not found"}

    # Parse URL
    import re
    pattern = r'mysql://(.*?):(.*?)@(.*?):(.*?)/(.*)'
    match = re.match(pattern, db_url)
    if not match:
        return {"error": "DATABASE_URL format invalid"}

    user, password, host, port, database = match.groups()

    # Path to the SQL file in container
    sql_file_path = "static/stunting.sql"

    # Run mysql import
    result = subprocess.run(
        [
            "mysql",
            f"-h{host}",
            f"-P{port}",
            f"-u{user}",
            f"-p{password}",
            database
        ],
        stdin=open(sql_file_path, "rb"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if result.returncode != 0:
        return {
            "error": result.stderr.decode()
        }

    return {"message": "SQL import successful"}
