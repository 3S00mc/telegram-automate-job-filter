from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

SESSION_NAME = "job_filter_session"

SUMMARY_HOUR = datetime.now().hour  # temporário para teste


SUMMARY_HOUR = 5  # 05h todo dia
# SUMMARY_HOUR = datetime.now().hour

ALLOWED_GROUPS = [
    -1001850877161,
    -1001052992679,
    -1001294628474
]
