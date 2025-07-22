# settings.py
# TODO: Centralized configuration for the Cloudana backend (dev/staging/prod)

from pydantic import BaseSettings, Field
from typing import Optional

class Settings(BaseSettings):
    # === Application ===
    APP_NAME: str = "Cloudana Backend"
    DEBUG: bool = True
    ENV: str = "development"  # development | staging | production

    # === Server ===
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # === Database ===
    DATABASE_URL: str = Field(..., env="DATABASE_URL")  # e.g., postgres://...

    # === Solana ===
    SOLANA_RPC_URL: str = Field(..., env="SOLANA_RPC_URL")  # e.g., https://api.mainnet-beta.solana.com
    SOLANA_KEYPAIR_PATH: str = Field(..., env="SOLANA_KEYPAIR_PATH")

    # === zkSNARK ===
    ZKEY_PATH: str = "cloudana/circuits/artifacts/hash_check/hash_check.zkey"
    VERIFICATION_KEY_PATH: str = "cloudana/circuits/artifacts/hash_check/verification_key.json"

    # === Redis / Queue (if used) ===
    REDIS_URL: Optional[str] = None

    # === Governance / DAO ===
    MIN_STAKE_FOR_PROPOSAL: int = 100  # Minimum CLD to submit proposals

    # === Security ===
    API_KEY: Optional[str] = None  # Optional header auth for slashing/reporting

    class Config:
        env_file = ".env"  # TODO: Create .env file in root or backend dir
        env_file_encoding = "utf-8"

# TODO: Create a singleton to access settings throughout the app
settings = Settings()
