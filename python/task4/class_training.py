"""
This module implements transport class as well as some
examples of inheritance
"""


class Transport:
    """
    This class implements basic transport fields and methods
    """
    name = 'transport'

    def __init__(self, fuel_capacity, max_speed, *args, **kwargs):
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
              f'capacity {self.fuel_capacity} liters and'
              f'maximum speed {self.max_speed} kph.')

    def time_and_fuel(self, distance):
        """
        This method counts expects distance as parameter.
        It returns time and amount of used fuel that it takes to
        cover the distance at maximum speed."""
        time = distance / self.max_speed
        fuel_used = 6 / 100 * distance
        return time, fuel_used


class TransportationVehicle(Transport):
    """
    This class implements basic transportation vehicle fields and methods
    """
    name = 'transportation vehicle'

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

    def time_and_fuel(self, distance):
        time, fuel = super().time_and_fuel(distance)
        return time, fuel * 100/6


class PassengerVehicle(Transport):
    """
    This class implements basic passenger vehicle fields and methods
    """
    name = 'passenger vehicle'

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

    def time_and_fuel(self, distance):
        time, fuel = super().time_and_fuel(distance)
        return time, fuel * 20/6


class MixedVehicle(PassengerVehicle, TransportationVehicle):
    """
    This class implements basic fields and methods of vehicle
    that can transport both passengers and cargo
    """
    name = 'mixed type vehicle'

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

    def time_and_fuel(self, distance):
        time, fuel = TransportationVehicle.time_and_fuel(self, distance)
        return time, fuel / 2
