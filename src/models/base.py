from abc import ABC, abstractmethod

class BaseModel(ABC):
    name: str

    @abstractmethod
    def build(self):
        pass
