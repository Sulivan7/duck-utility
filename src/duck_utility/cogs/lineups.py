"""Commands that show utility lineups."""

import discord
from discord import app_commands
from discord.ext import commands

from duck_utility.bot import DuckUtilityBot
from duck_utility.embeds import maps_embed, utility_embed

MAX_CHOICES = 25


class LineupsCog(commands.Cog):
    """The /smoke and /maps commands."""

    def __init__(self, bot: DuckUtilityBot) -> None:
        self.service = bot.utility_service

    @app_commands.command(name="smoke", description="Show a smoke lineup")
    @app_commands.rename(map_name="map")
    @app_commands.describe(
        map_name="The map, e.g. Mirage",
        position="Where to throw the smoke, e.g. Jungle",
    )
    async def smoke(
        self, interaction: discord.Interaction, map_name: str, position: str
    ) -> None:
        game_map = self.service.get_map(map_name)
        if game_map is None:
            available = ", ".join(m.name for m in self.service.list_maps())
            await interaction.response.send_message(
                f"❌ Map `{map_name}` not found.\nAvailable maps: {available}",
                ephemeral=True,
            )
            return

        utility = self.service.get_utility(map_name, position)
        if utility is None:
            available = ", ".join(u.name for u in game_map.utilities)
            await interaction.response.send_message(
                f"❌ Position `{position}` not found on {game_map.name}.\n"
                f"Available positions: {available}",
                ephemeral=True,
            )
            return

        await interaction.response.send_message(
            content="\n".join(utility.media),
            embed=utility_embed(game_map, utility),
        )

    @smoke.autocomplete("map_name")
    async def map_autocomplete(
        self, interaction: discord.Interaction, current: str
    ) -> list[app_commands.Choice[str]]:
        """Suggest maps while the user types."""
        maps = self.service.search_maps(current)
        return [app_commands.Choice(name=m.name, value=m.id) for m in maps][:MAX_CHOICES]

    @smoke.autocomplete("position")
    async def position_autocomplete(
        self, interaction: discord.Interaction, current: str
    ) -> list[app_commands.Choice[str]]:
        """Suggest positions of the map the user already picked."""
        map_name = interaction.namespace.map
        if not map_name:
            return []

        utilities = self.service.search_utilities(map_name, current)
        return [app_commands.Choice(name=u.name, value=u.id) for u in utilities][:MAX_CHOICES]

    @app_commands.command(name="maps", description="List the maps that have lineups")
    async def maps(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(embed=maps_embed(self.service.list_maps()))


async def setup(bot: DuckUtilityBot) -> None:
    """Called by `load_extension`: registers this cog in the bot."""
    await bot.add_cog(LineupsCog(bot))