# class_polymorphism.py
# Superhero & Vehicle Polymorphism Simulator

Welcome to the **Superhero & Vehicle Simulator** project!  
This program demonstrates the power of **Object-Oriented Programming (OOP)** using **Python** — particularly showcasing:

-  Class design and instantiation
-  Inheritance and method overriding
-  Polymorphism via shared method names with unique behaviors

---

##  Features

###  Superhero Class Hierarchy

- `Superhero`: Base class with shared attributes like `name`, `alias`, `power_level`, and `universe`
- Subclasses that override the `use_power()` method:
  - `FlyingHero`: Adds custom flying power message
  - `Speedster`: Adds super speed action
  - `Telepath`: Adds telepathy capabilities

Each subclass demonstrates **encapsulation** and **polymorphism**.

###  Vehicle Class Hierarchy

- `Vehicle`: Abstract-like base class with a `move()` method
- Subclasses include:
  - `Car`: Implements move with driving
  - `Plane`: Implements move with flying
  - `Boat`: Implements move with sailing

This section clearly shows **polymorphic behavior** using a common interface.

---

##  Installation & Execution

### 1️. Requirements

- Python 3.7+

### 2️. Running the Program

```bash
python superhero_polymorphism.py
