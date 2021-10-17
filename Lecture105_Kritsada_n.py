class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Pickup(Vehicle):
    color = ""

class Car(Vehicle):
    color = ""

class Van(Vehicle):
    color = ""

class Estatecar(Vehicle):
    color = ""


pickup1 = Pickup()
pickup1.turnOnAirConditioner()
pickup1.color = "red"

Car1 = Car()
Car1.turnOnAirConditioner()
Car1.color = "Blue"

Van1 = Van()
Van1.turnOnAirConditioner()
Van1.color = "Black"

Estatecar1 = Estatecar()
Estatecar1.turnOnAirConditioner()
Estatecar1.color = "Pink"


