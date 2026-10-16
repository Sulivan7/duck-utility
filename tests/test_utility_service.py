"""Tests for UtilityService, using the real data file."""

import pytest

from duck_utility.config import UTILITIES_FILE
from duck_utility.models.utility import UtilityType
from duck_utility.services.utility_service import UtilityService


@pytest.fixture
def service() -> UtilityService:
    return UtilityService.from_json(UTILITIES_FILE)


def test_loads_all_maps(service: UtilityService) -> None:
    map_ids = [game_map.id for game_map in service.list_maps()]

    assert map_ids == ["mirage", "inferno", "nuke", "overpass", "vertigo", "anubis", "dust2"]


def test_get_map_returns_the_map(service: UtilityService) -> None:
    game_map = service.get_map("mirage")

    assert game_map is not None
    assert game_map.name == "Mirage"


def test_get_map_returns_none_for_unknown_map(service: UtilityService) -> None:
    assert service.get_map("cache") is None


def test_get_utility_returns_the_utility(service: UtilityService) -> None:
    utility = service.get_utility("mirage", "jungle")

    assert utility is not None
    assert utility.name == "Jungle"
    assert utility.type is UtilityType.SMOKE
    assert len(utility.media) >= 1


def test_get_utility_returns_none_for_unknown_utility(service: UtilityService) -> None:
    assert service.get_utility("mirage", "banana") is None


def test_get_utility_returns_none_for_unknown_map(service: UtilityService) -> None:
    assert service.get_utility("cache", "jungle") is None


def test_every_utility_has_media(service: UtilityService) -> None:
    for game_map in service.list_maps():
        for utility in game_map.utilities:
            assert utility.media, f"{game_map.id}/{utility.id} has no media"


def test_get_map_ignores_case_and_spaces(service: UtilityService) -> None:
    game_map = service.get_map("  MiRaGe ")

    assert game_map is not None
    assert game_map.id == "mirage"


def test_get_map_accepts_the_display_name(service: UtilityService) -> None:
    game_map = service.get_map("Dust 2")

    assert game_map is not None
    assert game_map.id == "dust2"


def test_get_utility_accepts_the_display_name(service: UtilityService) -> None:
    utility = service.get_utility("mirage", "Market Window")

    assert utility is not None
    assert utility.id == "market-window"