
from unicodedata import name


class Product:
    '''Class doc.\n '''

    # Class variables
    iva = 0.17
    all = []

    def __init__(self, name: str, price: float, quantity = 0):
        '''This is the constructor, validation is made with assert statement \
            \nAssert statement checks whatever condition you want nigga, and you can attach an error messsage to the verificationclear\
            \nFormated string f"{}" allow you to write variables inside (interpolation)
        '''
        self.name = name
        self.price = price * self.iva
        self.quantity= quantity
        #validation 
        assert name.isidentifier(), f"{name} nao e um nome valido " 
        #Every new instance is added to the list of all objects of the class (in this case Product)
        Product.all.append(self)

    def showInfo(self):
        '''This method basically shows the info of the objects'''
        print(type(self))
        print(isinstance(self, Product))
        print("Name: ", self.name)
        print("price ", self.price)
        print("Quantity: ", self.quantity)
    
    def __repr__(self):
        '''This method allows you to represent the objects of this class ass you like'''
        return f"Product: ({self.name},{self.price},{self.quantity})"


    #staticmethods and classlevel methods   
    @staticmethod
    def changeIva(num):
        #does not pass the instance (self)
        Product.iva= num

    @classmethod
    def changeIva2(num):
        #This one throws an error if you don't put the self
        Product.iva= num

        

#Tests
# P1 = Product("Abobora",200)
# P1 = Product("Milho",300)
# P1.showInfo()
# #P1.iva = 0.15
# print(P1.iva)
# P1.changeIva(0.5)
# print("Novo iva de p1: ",P1.iva)

# # for obj in Product.all:
# #     print(obj.name)
# print(Product.all)
# #print(P1.__init__.__doc__)

# #isinstance

# a= 11.0

# print(isinstance(a,int))





