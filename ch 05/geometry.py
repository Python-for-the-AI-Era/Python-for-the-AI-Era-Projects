from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Tuple, Protocol, Iterator, Union

# --- THE DRAWABLE PROTOCOL ---

class Drawable(Protocol):
    def draw(self, canvas: str) -> str:
        """
        TODO: A Protocol confirming that any object implementing 
        draw() can be treated structural as a drawable entity.
        """
        ...


# --- ABSTRACT BASE CLASS ---

class Shape(ABC):
    
    @abstractmethod
    def area(self) -> float:
        pass
        
    @abstractmethod
    def perimeter(self) -> float:
        pass
        
    @abstractmethod
    def describe(self) -> str:
        pass

    # --- DUNDER OVERLOADS ---
    # TODO: Implement __repr__, __str__, __eq__ (by area), 
    # __lt__ (by area for sorting) and __add__ (for CompositeShape).


# --- FROZEN DATACLASSES ---

@dataclass(frozen=True)
class Circle(Shape):
    radius: float
    # TODO: Implement abstract methods and a read-only 'diameter' property

@dataclass(frozen=True)
class Rectangle(Shape):
    width: float
    height: float
    # TODO: Implement abstract methods, __contains__(point), and from_square(side) classmethod

@dataclass(frozen=True)
class Triangle(Shape):
    a: float
    b: float
    c: float

@dataclass(frozen=True)
class Ellipse(Shape):
    semi_major: float
    semi_minor: float

@dataclass(frozen=True)
class RegularPolygon(Shape):
    sides: int
    side_length: float


# --- COMPOSITE SHAPE (BONUS) ---

class CompositeShape(Shape):
    def __init__(self, shapes: List[Shape]):
        self.shapes = shapes
    # TODO: Implement Shape requirements based on cumulative child shape metrics


# --- COLLECTION CONTAINER ---

class ShapeCollection:
    def __init__(self, shapes: List[Shape] = None):
        self._shapes: List[Shape] = shapes if shapes else []

    # --- CONTAINER PROTOCOLS ---
    # TODO: Implement __iter__, __len__, __getitem__, __contains__

    # --- ANALYTICS ---
    def total_area(self) -> float:
        pass

    def largest(self) -> Shape:
        pass

    def smallest(self) -> Shape:
        pass

    def sorted_by_area(self) -> List[Shape]:
        pass


class Canvas:
    def __init__(self):
        self.elements: List[Drawable] = []
        
    def add(self, element: Drawable):
        self.elements.append(element)
        
    def render(self) -> str:
        # TODO: Loop through elements and execute their .draw() implementations
        pass


def main():
    print("Shape Geometry Library Initialized.")
    # 1. Instantiate various shapes
    # 2. Add them to a ShapeCollection
    # 3. Test built-ins: sorted(), min(), max() directly on the collection
    # 4. Demonstrate operator overloading: Shape + Shape -> CompositeShape
    pass

if __name__ == "__main__":
    main()