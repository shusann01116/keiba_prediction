# make python evaluate inside of defnition lines.
from __future__ import annotations

# List is required to import for typing.
from typing import List


class horse:
    def __init__(
        self, *args, id: int, name: str, weigth: int, parents: List[horse] = None
    ) -> None:
        self.id: int = id
        self.name: str | None = name
        self.weigth: int | None = weigth
        self.parents: List[horse] | None = parents


class track:
    def __init__(self, *args, id: int, name: str, place_id: int) -> None:
        self.id: int = id


class race:
    def __init__(self) -> None:
        self.id: int
        self.place_id: int
        self.race_card: List[horse]
