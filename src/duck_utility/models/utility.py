"""A single utility lineup and its type."""

from dataclasses import dataclass
from enum import StrEnum
from typing import Any


class UtilityType(StrEnum):
    """The kinds of grenades in CS2."""

    SMOKE = "smoke"
    FLASH = "flash"
    MOLOTOV = "molotov"
    HE = "he"


@dataclass(frozen=True)
class Utility:
    """A lineup: where to stand, where to aim and how to throw."""

    id: str
    name: str
    type: UtilityType
    media: tuple[str, ...]
    notes: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Utility:
        """Build a Utility from one entry of the JSON file."""
        return cls(
            id=data["id"],
            name=data["name"],
            type=UtilityType(data["type"]),
            media=tuple(data["media"]),
            notes=data.get("notes"),
        )