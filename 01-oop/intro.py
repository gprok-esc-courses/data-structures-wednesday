
class Car:
    def __init__(self, plate, km) -> None:
        self.plate = plate
        self.km = km

    def __str__(self) -> str:
        return self.plate + " km: " + str(self.km)
    

class Bus(Car):
    def __init__(self, plate, km, passengers) -> None:
        super().__init__(plate, km)
        self.passengers = passengers

    def __str__(self) -> str:
        return super().__str__() + " passengers: " + str(self.passengers)


a = Car("AAB6712", 1567)
b = Car("ZXA8711", 10987)
c = Bus("AOO8127", 12000, 45)

print(a)
print(b)
print(c)