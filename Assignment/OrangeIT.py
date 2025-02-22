class Controller:
    def __init__(self, acc_lst, product_lst):
        self.__acc_lst = acc_lst
        self.__product_lst = product_lst

    def search_acc_by_id(self,id):
        for i in self.__acc_lst:
            if i.get_acc_id() == id:
                return i
        
    def search_produch_by_name(self,name):
        for i in self.__product_lst:
            if name == i.get_name_product():
                return i
    def get_acc_lst(self):
        return self.__acc_lst
    
    def get_product_lst(self):
        return self.__product_lst

    def add_cart(self, product_name , quantity, acc_id):
        product = self.search_produch_by_name(product_name)
        acc = self.search_acc_by_id(acc_id)
        itemm = Cartitem(product,quantity)
        acc.add_cart_shopping(itemm)

class Account:
    def __init__(self,user_id , name , email):
        self.__id = user_id
        self.__name = name
        self.__email = email
    
    def get_acc_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
class Customer(Account):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.__myCart = Cart([])
        self.__myOrder = Order()
        self.__myReview = Review()

    def add_cart_shopping(self,cartitemm):
        self.__myCart.add_Cartitem(cartitemm)

    def get_cart_shopping(self): 
        return self.__myCart

class Admin(Account):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)

class Product:
    def __init__(self,product_id , name):
        self.__id = product_id
        self.__name = name
    
    def get_name_product(self):
        return self.__name

class Cart:
    def __init__(self,Cartitem_lst=[]):
        self.__Cartitem_lst = Cartitem_lst

    def add_Cartitem(self,inp):
        self.__Cartitem_lst.append(inp)

    def __str__(self):
        return f'{[[i.get_product().get_name_product(), i.get__quantity() ] for i in self.__Cartitem_lst]}'

class Cartitem:
    def __init__(self, product , quantity):
        self.__product = product
        self.__quantity = quantity

    def get_product(self):
        return self.__product
    
    def get__quantity(self):
        return self.__quantity
    
    def __str__(self):
        return f'{self.__product} : {self.__quantity}'
    
class Payment:
    pass

class QRcode(Payment):
    pass

class Card(Payment):
    pass

class Coupon:
    def __init__(self, id , name , discount , expire):
        self.__id = id
        self.__name = name
        self.__discount = discount
        self.__expire = expire

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_discount(self):
        return self.__discount

class Order:
    pass

class Review:
    pass

class Shipment:
    pass