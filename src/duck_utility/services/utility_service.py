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

    def get_map(self, map_id: str) -> GameMap | None:
        """Return the map with this id, or None if it doesn't exist."""
        return self._maps.get(map_id)

    def get_utility(self, map_id: str, utility_id: str) -> Utility | None:
        """Return one utility of a map, or None if the map or the utility doesn't exist."""
        game_map = self.get_map(map_id)
        if game_map is None:
            return None

        for utility in game_map.utilities:
            if utility.id == utility_id:
                return utility

        return None