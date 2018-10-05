from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

w = (150, 150, 150)
b = (0, 0, 255)
e = (0, 0, 0)


class GameArea:

    def __init__(self):
        self.area = [e, e, e, e, e, e, e, e,
                     e, e, e, e, e, e, e, e,
                     e, e, e, e, e, e, e, e,
                     e, e, e, e, e, e, e, e,
                     e, e, e, e, e, e, e, e,
                     e, e, e, e, e, e, e, e,
                     e, e, e, e, e, e, e, e,
                     e, e, e, e, e, e, e, e]

    def set_pixel(self, x, y=0, z=e):
        
        a = 8 * y
        b = a + x

        self.area[b] = z

    def show_area(self):
        sense.set_pixels(self.area)


comp_area = GameArea()

comp_area.set_pixel(1, 6, z=b)

comp_area.show_area()import
