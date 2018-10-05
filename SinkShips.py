from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

w = (150, 150, 150)
b = (0, 0, 255)
e = (0, 0, 0)


class GameArea:

    ships = [[[2,3,w],
              [3,3,w],
              [4,3,w]]]

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

    def set_ship(self, ship):
        for i in self.ships[ship]:
            self.set_pixel(i[0],
                           i[1],
                           i[2])


comp_area = GameArea()

#comp_area.set_pixel(1, 6, z=b)

comp_area.set_ship(0)

comp_area.show_area()
