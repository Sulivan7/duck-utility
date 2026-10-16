"""A CS2 map and its utilities."""

from dataclasses import dataclass
from typing import Any

from duck_utility.models.utility import Utility


@dataclass(frozen=True)
class GameMap:
    """A CS2 map, like Mirage or Inferno, with all its utilities."""

    id: str
    name: str
    utilities: tuple[Utility, ...]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> GameMap:
        """Build a GameMap (and its utilities) from one map of the JSON file."""
        return cls(
            id=data["id"],
            name=data["name"],
            utilities=tuple(Utility.from_dict(item) for item in data["utilities"]),
        )