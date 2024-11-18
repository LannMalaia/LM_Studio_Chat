from abc import ABC, abstractmethod

class Promptable(ABC):
    @abstractmethod
    def get_prompt(): pass
