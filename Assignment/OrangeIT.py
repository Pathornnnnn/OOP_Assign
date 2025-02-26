class Controller:
    def __init__(self, acc_lst, product_lst):
        self.__acc_lst = acc_lst
        self.__product_lst = product_lst

    def search_acc_by_id(self,id):
        for i in self.__acc_lst:
            if i.get_acc_id() == id:
                return i
            
    def search_acc_by_email(self, email):
        for acc in self.__acc_lst:
            if acc.get_acc_email() == email:
                return acc
        return None
        
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

    def get_lst_product(self):
        return self.__product_lst
    
    def search(self, name):
        result = []
        for product in self.__lst_product:
            if name.lower() in product.get_name().lower():
                result.append(product)
        return result
    
    def check_login(self, email, password):
        acc = self.search_acc_by_email(email)
        if isinstance(acc,Account):
            if acc.get_acc_email() == email and acc.get_password() == password:
                return acc
            else:
                return None
        return None  # ไม่ตรงกัน
    

class Account:
    id_acc = 1
    def __init__(self,name, email , password , age):
        self.__id = self.id_acc
        self.__name = name
        self.__email = email
        self.__password = password
        self.__age = age
        self.__myCart_shopping = Cart()
        self.id_acc +=1 

    def get_acc_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def get_email_acc(self):
        return self.__email
    
    def get_password_acc(self):
        return self.__password
    
class Customer(Account):
    def __init__(self, name, email , password , age):
        super().__init__( name, email , password , age)
        self.__myCart = Cart([])
        # self.__myOrder = Order()
        # self.__myReview = Review()

    def add_cart_shopping(self,cartitemm):
        self.__myCart.add_Cartitem(cartitemm)

    def get_cart_shopping(self): 
        return self.__myCart

    def get_acc_email(self):
        return self.get_email_acc()
    
    def get_password(self):
        return self.get_password_acc()
    
class Admin(Account):
    def __init__(self, name, email , password , age):
        super().__init__( name, email , password , age)

class Product:
    def __init__(self, name, price, description, stock ,img):
        self.__name = name
        self.__price = price
        self.__img = img
        self.__description = description
        self.__stock  = stock
    
    def get_name(self):
        return self.__name

    def get_acc_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password

    def get_price(self):
        return self.__price

    def get_img(self):
        return self.__img

    def get_description(self):
        return self.__description
    
    def get_stock(self):
        return self.__stock
    
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
    def __init__(self,id_pay , amount):
        self.__id = id_pay
        self.__amount = amount

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
    def __init__(self, Cart, Id, Date, Status, TotalAmount):
        self.__id = Id
        self.__list = Cart
        self.__Date = Date
        self.__Status = Status
        self.__TotalAmount = TotalAmount

class Review:
      def __init__(self, Id, product, rating , comment ):
        self.__id = Id
        self.__product = product
        self.__rating = rating
        self.__comment = comment

class Shipment:
    def __init__(self, id_ship , tracking_number , type_ship , date_ship):
        self.__id_ship = id_ship
        self.__tracking = tracking_number
        self.__type = type_ship
        self.__date = date_ship