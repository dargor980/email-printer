from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class ConfigEmail:
    email_user: str = os.getenv("EMAIL_USER")
    email_pass: str = os.getenv("EMAIL_PASSWORD")
    imap_server: str = os.getenv("IMAP_SERVER")