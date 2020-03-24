class Car:
    def __init__(self,speed,color):
        self.__speed = speed
        self.color = color
    def set_speed(self,value):
        self.__speed = value
    def get_speed(self):
        return self.__speed

bmw =Car(200,'black')
audi =Car(300,'red')
benz =Car(150,'browm')


benz.set_speed(250)
benz.__speed=400
print(audi.color)
print(benz.set_speed(256))
print(benz.get_speed())