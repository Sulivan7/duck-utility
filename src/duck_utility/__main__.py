"""Entry point: run the bot with `python -m duck_utility`."""

from duck_utility.bot import DuckUtilityBot
from duck_utility.config import Settings


def main() -> None:
    settings = Settings.from_env()
    bot = DuckUtilityBot()
    bot.run(settings.discord_token, root_logger=True)


if __name__ == "__main__":
    main()