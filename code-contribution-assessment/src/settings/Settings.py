from abc import ABC, abstractmethod


class Settings(ABC):
    pass

    @abstractmethod
    def set_settings(self):
        pass



