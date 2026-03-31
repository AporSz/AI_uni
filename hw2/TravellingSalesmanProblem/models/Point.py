import math
from dataclasses import dataclass

from hw2.TravellingSalesmanProblem.models.PointAbstract import PointAbstract

@dataclass
class Point(PointAbstract):
    x: float
    y: float
    nr: int

    def distance(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

