"""The Discord client of duck-utility."""

import logging

import discord
from discord.ext import commands

log = logging.getLogger(__name__)

EXTENSIONS = [
    "duck_utility.cogs.general",
]


class DuckUtilityBot(commands.Bot):
    """The bot itself: connects to Discord and loads the command groups."""

    def __init__(self) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned,
            intents=discord.Intents.default(),
        )

    async def setup_hook(self) -> None:
        """Run once, before the bot connects: load cogs and register slash commands."""
        for extension in EXTENSIONS:
            await self.load_extension(extension)

        synced = await self.tree.sync()
        log.info("Synced %d slash command(s)", len(synced))

    async def on_ready(self) -> None:
        """Run when the bot is connected and ready."""
        log.info("Logged in as %s", self.user)