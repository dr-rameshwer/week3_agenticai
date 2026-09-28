"""
Configuration and Settings Management
Course Instructor: Dr. Rameshwer

Uses Pydantic Settings to load and validate environment variables.
"""

import os
from typing import Optional
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

# Load .env if present
load_dotenv()

class Settings(BaseSettings):
    app_name: str = "Smart Student Academic Advisory Microservice"
    app_version: str = "1.0.0"
    instructor: str = "Dr. Rameshwer"
    app_env: str = "development"
    debug: bool = True
    app_host: str = "127.0.0.1"
    app_port: int = 8000

    # AI Model Credentials
    gemini_api_key: Optional[str] = os.getenv("GEMINI_API_KEY", None)
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()
