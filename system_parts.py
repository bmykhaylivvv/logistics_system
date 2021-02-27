import random
from typing import List


class Location:
    '''
    Represent a location of order.
    '''
    def __init__(self, city: str, postoffice: int):
        self.city = city
        self.postoffice = postoffice


class Item:
    '''
    Represent an order item.
    '''
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Name: {self.name} | Price: {self.price}"


class Vehicle:
    '''
    Represent delivery vehicle.
    '''
    def __init__(self, vehicleNo: int):
        self.vehicleNo = vehicleNo
        self.isAvailable = True

    def __str__(self):
        return f"Vehicle No.{self.vehicleNo} | status: {self.isAvailable}"


class Order:
    '''
    Represent an order with all properties.
    '''
    def __init__(self, user_name: str, city: str, postoffice: int, items: List[Item]):
        id = random.randint(10000, 100000)
        self.orderId = id
        self.user_name = user_name
        self.city = city
        self.postoffice = postoffice
        self.location = Location(city=self.city, postoffice=self.postoffice)
        self.items = items
        self.vehicle = None

    def __str__(self):
        return f"Youe order number is {self.orderId}"

    def calculateAmount(self):
        sum_ = 0
        for item in self.items:
            sum_ += item.price

        return sum_

    def assignVehicle(self, vehicle: Vehicle):
        return vehicle.isAvailable
