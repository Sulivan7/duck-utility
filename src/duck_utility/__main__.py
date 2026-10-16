"""Entry point: run the bot with `python -m duck_utility`."""

from duck_utility.bot import DuckUtilityBot
from duck_utility.config import UTILITIES_FILE, Settings
from duck_utility.services.utility_service import UtilityService


def main() -> None:
    settings = Settings.from_env()
    utility_service = UtilityService.from_json(UTILITIES_FILE)
    bot = DuckUtilityBot(utility_service)
    bot.run(settings.discord_token, root_logger=True)


if __name__ == "__main__":
    main()