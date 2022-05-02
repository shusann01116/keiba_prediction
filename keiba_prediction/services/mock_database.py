from typing import List

from core import interfaces
from core.types import horse


class MockHorses(interfaces.Ihorse_database):
    def __init__(self) -> None:
        self.horses: List[horse] = [
            horse(id=1, name="foo horse", weigth=23),
            horse(id=2, name="great kun", weigth=49),
            horse(id=3, name="ohhh ban", weigth=30),
            horse(id=4, name="Kitasan Black", weigth=11),
            horse(id=5, name="Sinboriru Dolf", weigth=200),
        ]

    def get_horse(self, id: int) -> horse:
        for h in self.horses:
            if h.id == id:
                return h

        return None
