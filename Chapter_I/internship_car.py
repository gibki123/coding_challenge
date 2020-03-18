from errors import IllegalCarError


class Car():

    def __init__(self, pax_count, car_mass, gear_count):
        if 1 > pax_count or pax_count > 5:
            raise IllegalCarError('Invalid pax_count value')
        if car_mass > 2000:
            raise IllegalCarError('Invalid car_mass value')
        self._pax_count = pax_count
        self._car_mass = car_mass
        self.gear_count = gear_count
        self.total_mass = car_mass + 70*pax_count

    @property
    def car_mass(self):
        return self._car_mass

    @car_mass.setter
    def car_mass(self, value):
        if value > 2000:
            raise IllegalCarError('Invalid car_mass value')
        self._car_mass = value

    @property
    def pax_count(self):
        return self._pax_count

    @pax_count.setter
    def pax_count(self, value):
        if 1 > value or value > 5:
            raise IllegalCarError('Invalid pax_count value')
        self._pax_count = value


if __name__ == '__main__':
    c = Car(2, 1000, 5)
    c.pax_count = 2200
    print(c.car_mass)
