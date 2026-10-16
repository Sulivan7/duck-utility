"""Tests for the embed builders, using small hand-made models."""

from duck_utility.embeds import help_embed, maps_embed, utility_embed
from duck_utility.models.game_map import GameMap
from duck_utility.models.utility import Utility, UtilityType

JUNGLE = Utility(
    id="jungle",
    name="Jungle",
    type=UtilityType.SMOKE,
    media=("https://example.com/jungle.gif",),
)
HEAVEN = Utility(
    id="heaven",
    name="Heaven",
    type=UtilityType.SMOKE,
    media=("https://example.com/heaven.gif",),
    notes="This is a W + jump throw",
)
MIRAGE = GameMap(id="mirage", name="Mirage", utilities=(JUNGLE, HEAVEN))


def test_utility_embed_title_has_map_and_position() -> None:
    embed = utility_embed(MIRAGE, JUNGLE)

    assert embed.title == "💨 Mirage — Jungle"


def test_utility_embed_without_notes_has_no_notes_field() -> None:
    embed = utility_embed(MIRAGE, JUNGLE)

    assert [field.name for field in embed.fields] == ["Type"]


def test_utility_embed_with_notes_shows_them() -> None:
    embed = utility_embed(MIRAGE, HEAVEN)

    assert embed.fields[-1].value == "This is a W + jump throw"


def test_maps_embed_has_one_field_per_map() -> None:
    embed = maps_embed([MIRAGE])

    assert len(embed.fields) == 1
    assert embed.fields[0].name == "Mirage"
    assert embed.fields[0].value == "2 lineups"


def test_help_embed_lists_the_commands() -> None:
    embed = help_embed([("ping", "Check if the bot is online")])

    assert embed.description == "`/ping` — Check if the bot is online"