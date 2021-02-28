'''
Main module for logistic system project.
'''
from typing import List
import random
from system_parts import Location, Item, Vehicle, Order


class LogisticSystem:
    '''
    Represent logistic system with all function.
    '''

    def __init__(self, vehicles: List[Vehicle]):
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order: Order):
        '''
        Register an order to the order list if there is available vehicle.
        '''
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                self.orders.append(order)
                vehicle.isAvailable = False
                return "Your order successfully added to our list"
                break
        else:
            return "There is no available vehicle to deliver an order."

    def trackOrder(self, orderId: int):
        '''
        Return order info if it exist, otherwise return "No such order."
        '''
        for order in self.orders:
            if order.orderId == orderId:
                return f"Your order #{orderId} is sent to {order.city}. Total price: {order.calculateAmount()} UAH"

        else:
            return "No such order."


# ------------------------------------------------------------------------------------------------------------------------
# You can use it with random seed (e.g. random.seed(10))
# random.seed(10)
vehicles = [Vehicle(1), Vehicle(2)]
logSystem = LogisticSystem(vehicles)
my_items = [Item('book', 110), Item('chupachups', 44)]
my_order1 = Order(user_name='Oleg', city='Lviv', postoffice=53, items=my_items)
print("----------")
print("You`ve create an order, info BELOW.")
print(my_order1)
print()
print(logSystem.placeOrder(my_order1))
# e.g. print(logSystem.trackOrder(84894)), if you use seed(10)
print(logSystem.trackOrder(my_order1.orderId))
print("----------")


print("==========")


my_items2 = [Item('flowers', 11), Item('shoes', 153), Item('helicopter', 0.33)]
my_order2 = Order('Andrii', 'Odessa', 3, my_items2)
print("----------")
print("You`ve create an order, info BELOW.")
print(my_order2)
print()
print(logSystem.placeOrder(my_order2))
# e.g. print(logSystem.trackOrder(14270)), if you use seed(10)
print(logSystem.trackOrder(my_order2.orderId))
print("----------")


print("==========")


my_items3 = [Item('coat', 61.8), Item('shower', 5070), Item('rollers', 700)]
my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)
print("----------")
print("You`ve create an order, info BELOW.")
print(my_order3)
print()
print(logSystem.placeOrder(my_order3))
# e.g. print(logSystem.trackOrder(66215)), if you use seed(10)
print(logSystem.trackOrder(my_order3.orderId))
print("----------")
