from tkinter import N

from unicodedata import name
from ElectronicDevice import ElectronicDevice

from object import Product


class Celphone(Product,ElectronicDevice):
    def __init__(self, name: str, price: float, quantity=0, ):
        super().__init__(name, price, quantity)

