from abc import ABC, abstractmethod


class Request(ABC):
    pass

    @abstractmethod
    def implement(self):
        pass
