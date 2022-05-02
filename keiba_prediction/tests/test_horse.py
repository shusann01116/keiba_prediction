from core.interfaces import Ihorse_database
from core.types import horse
from services import mock_database

database: Ihorse_database = mock_database.MockHorses()


def test_get_horse():
    validate_horse = horse(id=2, name="great kun", weigth=49)

    h = database.get_horse(id=2)

    assert h.id == validate_horse.id
    assert h.name == validate_horse.name
    assert h.weigth == validate_horse.weigth


def test_get_horse_return_none():
    h = database.get_horse(20000)

    assert h is None
