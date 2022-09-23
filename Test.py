
from Celphone import Celphone
from object import Product


cell1 = Celphone("tecno",100,1,31)
print(cell1.name)
print(cell1.showInfo())
print("========================================================")
Product.changeIva(0.8)
cell1 = Celphone("tecno2",100,1,31)
print(cell1.showInfo())
