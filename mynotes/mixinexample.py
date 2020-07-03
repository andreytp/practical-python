#mixinexample.py

class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'

class Bike:
    def noise(self):
        return 'On Your Left'

    def pedal(self):
        return 'Pedaling!'
        
class Loud:
    def noise(self):
        return super().noise().upper()
        
        
class LoudDog(Loud, Dog):
    pass

class LoudBike(Loud, Bike):
    pass