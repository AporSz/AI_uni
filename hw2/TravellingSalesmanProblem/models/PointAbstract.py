from abc import ABC, abstractmethod

class PointAbstract(ABC):
    @abstractmethod
    def distance(self, point):
        pass