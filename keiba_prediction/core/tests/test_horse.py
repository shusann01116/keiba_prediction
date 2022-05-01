from keiba_prediction.core.types import horse, horses

horses_instance = horses()


def test_add_horse():
    horses_instance.add_horse(horse(id=2, name="Kazi", weigth=32, parents=None))


def test_get_horse():
    horses_instance.add_horse(horse(id=1, name="Kazu", weigth=32, parents=None))
    horses_instance.add_horse(horse(id=2, name="Kazi", weigth=33, parents=None))

    validate_horse = horse(id=1, name="Kazu", weigth=32)

    test_horse: horse = horses_instance.get_horse(id=1)
    assert validate_horse.id == test_horse.id
    assert validate_horse.name == test_horse.name
    assert validate_horse.weigth == test_horse.weigth
    assert validate_horse.parents == test_horse.parents

    test_horse: horse = horses_instance.get_horse(id=2)
    assert validate_horse != test_horse
