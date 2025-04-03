
class Car:

    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.speed = 20

class FastCar(Car):

    def __init__(self, x, y):
        super().__init__(x,y)
        self.speed = 100


if __name__ == '__main__':


    car_a = Car(10,20)
    car_b = Car( 20, 20)

