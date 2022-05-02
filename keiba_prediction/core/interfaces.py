import abc

from core.types import horse


class Ihorse_database(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_horse(self, id: int) -> horse:
        return NotImplementedError()
