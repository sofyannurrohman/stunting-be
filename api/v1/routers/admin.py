import os
from fastapi import APIRouter
import subprocess
from urllib.parse import urlparse

router = APIRouter()

@router.post("/import-sql")
def import_sql():
    try:
        db_url = os.getenv("DATABASE_URL")
        if not db_url:
            return {"error": "DATABASE_URL not found"}

        parsed = urlparse(db_url)
        user = parsed.username
        password = parsed.password
        host = parsed.hostname
        port = str(parsed.port)
        database = parsed.path.lstrip('/')

        sql_file_path = "static/stunting.sql"

        if not os.path.exists(sql_file_path):
            return {"error": f"SQL file not found at path: {sql_file_path}"}

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

    except Exception as e:
        return {"error": str(e)}
