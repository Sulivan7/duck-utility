"""Application settings loaded from environment variables."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    """All the configuration the bot needs to run."""

    discord_token: str

    @classmethod
    def from_env(cls) -> Settings:
        """Read the settings from the `.env` file and environment variables."""
        load_dotenv()

        token = os.getenv("DISCORD_TOKEN")
        if not token:
            raise RuntimeError("DISCORD_TOKEN is not set. Create a .env file (see README).")

        return cls(discord_token=token)