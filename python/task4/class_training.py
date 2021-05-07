"""
This module implements transport class as well as some
examples of inheritance
"""


class Transport:
    """
    This class implements basic transport fields and methods
    """
    name = 'transport'
    license_needed = ''

    def __init__(self, fuel_capacity, max_speed):
        """
        It is the innit of Transport class. It expects
        fuel capacity in liters as first parameter
        and maximum speed in kph as second parameter
        """
        self.fuel_capacity = fuel_capacity
        self.max_speed = max_speed

    def info(self):
        """This method describes the transport"""
        print(f'I am a {self.name} with fuel '
              f'capacity {self.fuel_capacity} liters and '
              f'maximum speed {self.max_speed} kph.')

    def time_to_travel(self, distance):
        """
        This method expects distance as parameter.
        It returns time that it takes to
        cover the distance at maximum speed.
        """
        return distance / self.max_speed

    @staticmethod
    def fuel(distance):
        """
        This method expects distance as parameter.
        It returns amount of used fuel that it takes to
        cover the distance at maximum speed.
        """
        return 6 / 100 * distance

    @property
    def engine_sound(self):
        """This method returns sound of engine of this transport"""
        return 'not defined'

    @classmethod
    def license(cls):
        """
        This method shows you which type of driver license you
         need in order to drive this transport
         """
        print(f'You need {cls.license_needed} to drive {cls.name}')


class PersonalTransport(Transport):
    """
    This class implements basic transport fields and methods
    """
    name = 'personal transport'
    license_needed = 'BE'

    @property
    def engine_sound(self):
        return '*voorrr-voorrr-voorrr*'


class TransportationVehicle(Transport):
    """
    This class implements basic transportation vehicle fields and methods
    """
    name = 'transportation vehicle'
    license_needed = 'CE'

    def __init__(self, fuel_capacity, max_speed,
                 cargo_weight, *args, **kwargs):
        """
        It is the innit of TransportationVehicle class. It expects
        fuel capacity in liters as first parameter, maximum
        speed in kph as second parameter and maximum cargo weight
        in kg as  third parameter.
        """
        super().__init__(fuel_capacity, max_speed, *args, **kwargs)
        self.cargo_weight = cargo_weight

    def info(self):
        """This method describes the transportation vehicle"""
        super().info()
        print(f'My maximum cargo weight is {self.cargo_weight} kg.')

    def fuel(self, distance):
        return super().fuel(distance) * 100/6

    @property
    def engine_sound(self):
        return '*thump-thump-thump*'


class PassengerVehicle(Transport):
    """
    This class implements basic passenger vehicle fields and methods
    """
    name = 'passenger vehicle'
    license_needed = 'BE'

    def __init__(self, fuel_capacity, max_speed, passengers, *args, **kwargs):
        """
        It is the innit of PassengerVehicle class. It expects fuel
        capacity in liters as first parameter, maximum speed in
        kph as second parameter and maximum passengers
        number as  third parameter.
        """
        super().__init__(fuel_capacity, max_speed, *args, **kwargs)
        self.passengers = passengers

    def info(self):
        """This method describes the passenger vehicle"""
        super().info()
        print(f'My maximum passengers number is {self.passengers}.')

    def fuel(self, distance):
        return super().fuel(distance) * 20/6

    @property
    def engine_sound(self):
        return '*rump-rump-rump*'


class MixedVehicle(PassengerVehicle, TransportationVehicle):
    """
    This class implements basic fields and methods of vehicle
    that can transport both passengers and cargo
    """
    name = 'mixed type vehicle'
    license_needed = 'DE'

    def __init__(self, fuel_capacity, max_speed,
                 passengers, cargo_weight, *args, **kwargs):
        """
        It is the innit of MixedVehicle class. It expects fuel
        capacity in liters as first parameter, maximum speed
        in kph as second parameter, maximum maximum passengers
        number as third parameter and cargo weight in kg as
        fourth parameter.
        """
        super().__init__(fuel_capacity, max_speed,
                         passengers=passengers, cargo_weight=cargo_weight)

    def fuel(self, distance):
        return super().fuel(distance) * 6/40

    @property
    def engine_sound(self):
        return '*ch-sh-ch-sh*'


car = PersonalTransport(80, 200)
car.info()
print(f'It needs {car.time_to_travel(100)} hours and {car.fuel(100)} '
      f'liters of fuel to travel 100 km.\n'
      f'It sounds like {car.engine_sound}. You need {car.license()} '
      f'in order to drive it\n')
truck = TransportationVehicle(350, 100, 10000)
truck.info()
print(f'It needs {truck.time_to_travel(100)} hours and {truck.fuel(100)} '
      f'liters of fuel to travel 100 km.\n'
      f'It sounds like {truck.engine_sound}. You need {truck.license()} '
      f'in order to drive it\n')
ambulance = PassengerVehicle(250, 150, 7)
ambulance.info()
print(f'It needs {ambulance.time_to_travel(100)} hours and '
      f'{ambulance.fuel(100)} liters of fuel to travel 100 km.\n'
      f'It sounds like {ambulance.engine_sound}. You need '
      f'{ambulance.license()} in order to drive it\n')
bus = MixedVehicle(400, 140, 7, 1000)
bus.info()
print(f'It needs {bus.time_to_travel(100)} hours and {bus.fuel(100)} '
      f'liters of fuel to travel 100 km.\n'
      f'It sounds like {bus.engine_sound}. You need '
      f'{bus.license()} in order to drive it\n')
