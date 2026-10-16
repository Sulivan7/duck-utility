"""Find maps and utilities in the lineup data."""

import json
from pathlib import Path

from duck_utility.models.game_map import GameMap
from duck_utility.models.utility import Utility


class UtilityService:
    """Answers questions like "which smokes exist on Mirage?"."""

    def __init__(self, maps: list[GameMap]) -> None:
        self._maps = {game_map.id: game_map for game_map in maps}

    @classmethod
    def from_json(cls, path: Path) -> UtilityService:
        """Load every map and utility from a JSON file."""
        data = json.loads(path.read_text(encoding="utf-8"))
        return cls([GameMap.from_dict(item) for item in data["maps"]])

    def list_maps(self) -> list[GameMap]:
        """Return all maps, in the same order as the JSON file."""
        return list(self._maps.values())

    def get_map(self, map_name: str) -> GameMap | None:
        """Find a map by id or name (case and spaces don't matter), or return None."""
        query = _normalize(map_name)
        for game_map in self._maps.values():
            if query in (game_map.id, _normalize(game_map.name)):
                return game_map

        return None

    def get_utility(self, map_name: str, utility_name: str) -> Utility | None:
        """Find a utility of a map by id or name, or return None."""
        game_map = self.get_map(map_name)
        if game_map is None:
            return None

        query = _normalize(utility_name)
        for utility in game_map.utilities:
            if query in (utility.id, _normalize(utility.name)):
                return utility

        return None


def _normalize(text: str) -> str:
    """Turn user input like "  Market   Window " into "market-window"."""
    return "-".join(text.lower().split())