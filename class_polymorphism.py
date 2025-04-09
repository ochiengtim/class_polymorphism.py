# Superhero Class System

class Superhero:
    def __init__(self, name, alias, power_level, universe):
        self.name = name
        self.alias = alias
        self.power_level = power_level
        self.universe = universe

    def introduce(self):
        print(f"I am {self.alias}, also known as {self.name} from the {self.universe} universe!")

    def use_power(self):
        print(f"{self.alias} uses a generic power. ")


class FlyingHero(Superhero):
    def use_power(self):
        print(f"{self.alias} takes to the skies!  Soaring through the clouds!")


class Speedster(Superhero):
    def use_power(self):
        print(f"{self.alias} blurs past in a flash of light! Speed unmatched!")


class Telepath(Superhero):
    def use_power(self):
        print(f"{self.alias} reads minds and controls thoughts. Telepathy engaged!")


# Polymorphism Challenge - Vehicle System

class Vehicle:
    def move(self):
        print("The vehicle moves forward.")


class Car(Vehicle):
    def move(self):
        print("Driving on the road...")


class Plane(Vehicle):
    def move(self):
        print("Flying through the skies...")


class Boat(Vehicle):
    def move(self):
        print("Sailing across the sea...")


#Runtime Test Zone
if __name__ == "__main__":
    # Superhero Instances
    h1 = FlyingHero("Clark Kent", "Superman", 99, "DC")
    h2 = Speedster("Barry Allen", "The Flash", 95, "DC")
    h3 = Telepath("Jean Grey", "Phoenix", 98, "Marvel")

    h1.introduce()
    h1.use_power()
    print()

    h2.introduce()
    h2.use_power()
    print()

    h3.introduce()
    h3.use_power()
    print()

    # Vehicle Instances with Polymorphic move()
    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
        v.move()
