# Project 05: Shape Geometry Library

### Overview
This project brings together the entire Object-Oriented Programming (OOP) paradigm in Python. Rather than writing basic objects, you will implement a strongly integrated domain library using strict inheritance (`ABC`), structural subtyping (`Protocols`), value guarantees (`frozen dataclasses`), custom collection sequences, and complete rich-comparison operator overloading.

---

### The Architecture Contract

Your implementation must fulfill these specific OOP conditions:

#### 1. Polymorphism and Dunder Operators
Your abstract base class `Shape` acts as the explicit behavioral blueprint. All concrete shapes inherit from it. 
* To support native python operations, you must overload the following dunder methods on the base `Shape` class so they apply automatically across all subclasses:
  - `__eq__` & `__lt__`: Compare objects purely by their calculated `.area()`. This unlocks Python's built-in sorting and evaluation behaviors (`sorted()`, `min()`, `max()`) without requiring custom sorting lambda keys.
  - `__add__`: Must allow adding any two geometric entities together (e.g., `Circle(5) + Rectangle(4, 6)`), returning a unified `CompositeShape` containing both entities.

#### 2. Immutable Value States (`frozen=True`)
Concrete configurations must be declared as **frozen dataclasses**. This locks their attributes upon instantiation, ensuring that their underlying math properties cannot be mutated at runtime.

#### 3. Custom Sequence Protocols
Your `ShapeCollection` is an object container. Instead of making users access internal list pointers (like `collection.shapes[0]`), implement the standard collection dunders:
* `__len__`: Allows running `len(collection)`.
* `__getitem__`: Allows absolute array indexing like `collection[0]`.
* `__iter__`: Allows direct looping paths (`for shape in collection:`).
* `__contains__`: Integrates clean boolean containment queries (`if circle in collection:`).

#### 4. Nominal vs. Structural Typing (`Protocols`)
While shapes use rigid nominal inheritance (`Circle` *is a* `Shape`), your rendering engine must use structural typing through a `Drawable` `Protocol`. Any class that implements a `draw(canvas: str) -> str` signature instantly becomes matchable as a `Drawable` type, even if it does not belong to the `Shape` object hierarchy.

---

### Technical Signposts & Hints

#### 1. Checking Points inside Rectangles (`__contains__`)
Overloading `__contains__` on your `Rectangle` class allows you to check if an $(x, y)$ coordinate is inside its geometry using the `in` keyword:
```python
def __contains__(self, point: Tuple[float, float]) -> bool:
    x, y = point
    return 0 <= x <= self.width and 0 <= y <= self.height

```

#### 2. Regular Polygon Mathematical Trick

To determine the area of a regular $n$-sided polygon using only its number of sides ($n$) and side length ($s$), use the standard trigonometric formula:


$$\text{Area} = \frac{n \times s^2}{4 \times \tan\left(\frac{\pi}{n}\right)}$$

* *Hint*: Remember to import `math` and use `math.tan` along with `math.pi`.

---

### Constraints Checklist

* [ ] No attributes can be altered after a concrete shape is created (`frozen=True` compliance).
* [ ] Direct rich comparison operators must not be manually rewritten inside individual concrete shapes; handle this in the base class.
* [ ] The `ShapeCollection` must pass elements straight to built-in functions (`min()`, `max()`, `sorted()`) naturally without auxiliary property extraction keys.
* [ ] Every class method, getter property, and dunder definition must carry complete static type annotations.

```

---

### Why this works perfectly for Chapter 05:
* **Rich Comparisons**: By implementing `__lt__` and `__eq__` inside the abstract class, students see the real magic of OOP: writing code *once* that gives 5 separate subclasses the power to be sorted instantly.
* **Dataclass Integration**: It breaks the myth that dataclasses are only for simple database rows, proving they can fully integrate into complex abstract mathematical frameworks.

```