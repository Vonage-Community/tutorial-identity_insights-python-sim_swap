# jwt_helper.py
import time
import jwt
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APPLICATION_ID")
PRIVATE_KEY_PATH = "private.key"

def generate_jwt():
    private_key = Path(PRIVATE_KEY_PATH).read_text()
    now = int(time.time())
    payload = {
        "application_id": APP_ID,
        "iat": now,
        "exp": now + 300,  # 5 minutes
        "jti": f"SIMSWAP-{now}"
    }
    return jwt.encode(payload, private_key, algorithm="RS256")
