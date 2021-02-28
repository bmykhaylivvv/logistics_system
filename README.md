# Logistics system
***Logistics system*** -- program represents a simple version of logistics system.

## Main files
- **system_parts.py** -- module with required functions for logistics system.
- **logistic_system.py** -- main module which contains main functions of program.

## How it works?
Program run only via code in *logistic_system.py* module.

***Example of functions execution:***
```   
>>> vehicles = [Vehicle(1), Vehicle(2)]
>>> logSystem = LogisticSystem(vehicles)
>>> my_items = [Item('book',110), Item('chupachups',44)]
>>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
Your order number is 165488695.

>>> logSystem.placeOrder(my_order)
>>> logSystem.trackOrder(165488695)
Your order #165488695 is sent to Lviv. Total price: 154 UAH.

>>> my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
>>> my_order2 = Order('Andrii', 'Odessa', 3, my_items2)
Your order number is 234976475.

>>> logSystem.placeOrder(my_order2)
>>> logSystem.trackOrder(234976475)
Your order #234976475 is sent to Odessa. Total price: 164.33 UAH.

>>> my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]
>>> my_order3 = Order(Olesya, 'Kharkiv', 17, my_items3)
Your order number is 485932990.

>>> logSystem.placeOrder(my_order3)
There is no available vehicle to deliver an order.

>>> logSystem.trackOrder(485932990)
No such order.
``` 