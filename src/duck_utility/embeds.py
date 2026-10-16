"""Build the Discord embeds (the colored cards) that the bot sends."""

import discord

from duck_utility.models.game_map import GameMap
from duck_utility.models.utility import Utility, UtilityType

BRAND_COLOR = discord.Colour(0xF5C518)
CREDITS = "Lineups from Tactical Toss Tutor"

UTILITY_STYLES = {
    UtilityType.SMOKE: ("💨", "Smoke", discord.Colour(0x9E9E9E)),
    UtilityType.FLASH: ("⚡", "Flash", discord.Colour(0xFFEB3B)),
    UtilityType.MOLOTOV: ("🔥", "Molotov", discord.Colour(0xFF5722)),
    UtilityType.HE: ("💣", "HE grenade", discord.Colour(0x4CAF50)),
}


def utility_embed(game_map: GameMap, utility: Utility) -> discord.Embed:
    """Card with the title, type and notes of one lineup."""
    emoji, label, color = UTILITY_STYLES[utility.type]

    embed = discord.Embed(title=f"{emoji} {game_map.name} — {utility.name}", color=color)
    embed.add_field(name="Type", value=label)
    if utility.notes:
        embed.add_field(name="⚠️ Notes", value=utility.notes, inline=False)
    embed.set_footer(text=CREDITS)
    return embed


def maps_embed(maps: list[GameMap]) -> discord.Embed:
    """Card with every map and how many lineups it has."""
    embed = discord.Embed(title="🗺️ Available maps", color=BRAND_COLOR)
    for game_map in maps:
        embed.add_field(name=game_map.name, value=f"{len(game_map.utilities)} lineups")
    embed.set_footer(text="Use /smoke <map> <position> to see a lineup")
    return embed


def help_embed(commands: list[tuple[str, str]]) -> discord.Embed:
    """Card that lists the bot commands, given as (name, description) pairs."""
    lines = [f"`/{name}` — {description}" for name, description in commands]
    return discord.Embed(
        title="🦆 Duck Utility — Commands",
        description="\n".join(lines),
        color=BRAND_COLOR,
    )