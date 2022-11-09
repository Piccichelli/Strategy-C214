from abc import ABC, abstractclassmethod

class ListOrderingStrategy(ABC):
    @abstractclassmethod
    def sort(self, lista):
        pass