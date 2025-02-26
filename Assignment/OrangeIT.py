class Controller:
    def __init__(self, acc_lst, product_lst):
        self.__acc_lst = acc_lst
        self.__product_lst = product_lst

    def search_acc_by_id(self,acc_id):
        for i in self.__acc_lst:
            if i.get_acc_id() == acc_id:
                return i
            
    def search_acc_by_email(self, email):
        for acc in self.__acc_lst:
            if acc.get_acc_email() == email:
                return acc
        return None
    
    def search_product_by_id(self, product_id):
        for i in self.__product_lst:
            if product_id == i.get_id():
                return i
        
            
    def search_product_by_name(self,name):
        for i in self.__product_lst:
            if name == i.get_name():
                return i
    def get_acc_lst(self):
        return self.__acc_lst
    
    def get_product_lst(self):
        return self.__product_lst

    def add_to_cart(self, product_id , quantity, acc_id):
        product = self.search_product_by_id(product_id)
        acc = self.search_acc_by_id(acc_id)
        stock_product = product.get_stock()
        if stock_product >= quantity:
            itemm = Cartitem(product,quantity)
            acc.Add_to_cart_shopping(itemm)
            return True

        else:
            return False

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
        self.__id = Account.id_acc
        self.__name = name
        self.__email = email
        self.__password = password
        self.__age = age
        Account.id_acc +=1 

    def get_acc_id(self):
        return self.__id

    def get_acc_name(self):
        return self.__name
    
    def get_email_acc(self):
        return self.__email
    
    def get_password_acc(self):
        return self.__password

    # def get_cart_shopping(self):
    #     return self.__myCart_shopping
    
    # def Add_to_cart_shopping(self,cartitem):
    #     self.__myCart_shopping.add_to_cartitem(cartitem)

    def get_cart_shopping(self):
        return self.__myCart_shopping
    
    
class Customer(Account):
    def __init__(self, name, email , password , age):
        super().__init__( name, email , password , age)
        self.__myCart_shopping = Cart([])
        # self.__myOrder = Order()
        # self.__myReview = Review()

    def get_cart_shopping(self): 
        return self.__myCart

    def get_acc_email(self):
        return self.get_email_acc()
    
    def get_password(self):
        return self.get_password_acc()
    
    def get_id(self):
        return super().get_acc_id()
    
    def get_name(self):
        return super().get_acc_name()
    
    def get_cart_shopping(self):
        return self.__myCart_shopping
    
    def Add_to_cart_shopping(self,cartitem):
        self.__myCart_shopping.add_to_cartitem(cartitem)

class Admin(Account):
    def __init__(self, name, email , password , age):
        super().__init__( name, email , password , age)

class Product:
    product_id = 1
    def __init__(self, name, price, description, stock ,img):
        self.__id = Product.product_id
        self.__name = name
        self.__price = price
        self.__img = img
        self.__description = description
        self.__stock  = stock
        Product.product_id += 1

    def get_id(self):
        return self.__id
    
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

    def add_to_cartitem(self,inp):
        self.__Cartitem_lst.append(inp)

    def __str__(self):
        return f'{[[i.get_product().get_name(), i.get__quantity() ] for i in self.__Cartitem_lst]}'

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