import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL") or "mysql+pymysql://app_user:password@localhost/shop"


settings = Settings()
