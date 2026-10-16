"""General-purpose commands, not tied to lineups."""

import discord
from discord import app_commands
from discord.ext import commands

from duck_utility.embeds import help_embed


class GeneralCog(commands.Cog):
    """Basic commands like /ping and /help."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="ping", description="Check if the bot is online")
    async def ping(self, interaction: discord.Interaction) -> None:
        latency_ms = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"🏓 Pong! `{latency_ms} ms`")

    @app_commands.command(name="help", description="Show all the bot commands")
    async def help(self, interaction: discord.Interaction) -> None:
        commands_info = sorted(
            (command.name, command.description)
            for command in self.bot.tree.get_commands()
            if isinstance(command, app_commands.Command)
        )
        await interaction.response.send_message(embed=help_embed(commands_info))


async def setup(bot: commands.Bot) -> None:
    """Called by `load_extension`: registers this cog in the bot."""
    await bot.add_cog(GeneralCog(bot))