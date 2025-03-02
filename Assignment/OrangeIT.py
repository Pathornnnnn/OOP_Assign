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
        stock_product = product.get_stock()
        acc = self.search_acc_by_id(acc_id)
        print(product,stock_product,acc)
        if stock_product >= quantity:
            for i in acc.get_cart_shopping().get_cart_lst():
                if product.get_name() == i.get_product().get_name():
                    i.add_quantity(quantity)
                    product.down_stock(quantity)
                    print('add to cart exist item')
                    return True
            itemm = Cartitem(product,quantity)
            acc.Add_to_cart_shopping(itemm)
            product.down_stock(quantity)
            print('add to cart new item')
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
    
    def update_cart_quantity(self , account , cartitem_id , quantity):
        acc = self.search_acc_by_id(account)
        cart = acc.get_cart_shopping()
        cartitems = acc.get_cart_shopping().get_cart_lst()
        for i in cartitems:
            if i.get_id() == cartitem_id:
                stock = i.get_product().get_stock()
                if i.get_quantity() + quantity <= stock and i.get_quantity() + quantity > 0:
                    i.update_quantity(quantity)
                    print('Update Pass')
                    return True
                else:
                    print('Can"t Update stock not enough')
                    return False
        return False

    def remove_cartitem_by_id(self , account , cartitem_id):
        acc = self.search_acc_by_id(account)
        cart = acc.get_cart_shopping()
        cart.remove_cartitem(cartitem_id)
        print('Remove Success')

    def creat_order_acc(self, account , name , addr , city , post , phone):
        acc = self.search_acc_by_id(account)
        cart = acc.get_cart_shopping()
        cart_lst = acc.get_cart_shopping().get_cart_lst()
        address = Address(name, addr, city , post, phone)
        my_order = Order(cart_lst , address , 'Wait For payment' , cart.get_price_total())
        acc.add_myorder(my_order)
        print('add myorder')
        return my_order.get_id()
    
    def change_status_order(self, account , order_id , message):
        acc = self.search_acc_by_id(account)
        order_lst = acc.get_myorder_lst()
        for i in order_lst:
            if i.get_id() == order_id:
                i.update_status(message)
                print('Update status success')
                return True
            
        print('can not update')
        return False
    
    def clear_cart_account_by_id(self,account ):
        acc = self.search_acc_by_id(account)
        cart = acc.get_cart_shopping()
        cart.clear_cart()
        return True
    
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
        self.__myOrder = []
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
    
    def get_myorder_lst(self):
        return self.__myOrder
    
    def add_myorder(self,order):
        self.__myOrder.append(order)
        return True
    
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
    
    def down_stock(self, quantity):
        self.__stock -= quantity
    
class Cart:
    def __init__(self,Cartitem_lst=[]):
        self.__Cartitem_lst = Cartitem_lst

    def add_to_cartitem(self,inp):
        self.__Cartitem_lst.append(inp)

    def get_cart_lst(self):
        return self.__Cartitem_lst

    def get_price_total(self):
        total = 0
        for i in self.__Cartitem_lst:
            total += i.get_product().get_price() * i.get_quantity()
        return total
    
    def search_cartitem_by_id(self, cartitem_id):
        for i in self.__Cartitem_lst:
            if i.get_id() == cartitem_id:
                return i

    def remove_cartitem(self, cartitem_id):
        obj = self.search_cartitem_by_id(cartitem_id)
        self.__Cartitem_lst.remove(obj)
        return True
    
    def clear_cart(self):
        self.__Cartitem_lst = []
        print('clear cart success')
    
    def __str__(self):
        return f'{[[i.get_product().get_name(), i.get_quantity() ] for i in self.__Cartitem_lst]}'

class Cartitem:
    id_cartitem = 1
    def __init__(self, product , quantity):
        self.__id_cartitem = Cartitem.id_cartitem
        self.__product = product
        self.__quantity = quantity
        Cartitem.id_cartitem += 1

    def get_id(self):
        return self.__id_cartitem
    
    def get_product(self):
        return self.__product
    
    def get_quantity(self):
        return self.__quantity
    
    def add_quantity(self, quantity):
        self.__quantity += quantity
    
    def __str__(self):
        return f'{self.__product} : {self.__quantity}'
    
    def get_price_product(self):
        return self.get_product().get_price()
    
    def update_quantity(self, n_quan):
        self.__quantity += n_quan
        print('Update success')
    
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
    order_id = 1
    def __init__(self, Cartitem_lst, Address, Status, TotalAmount):
        self.__id = Order.order_id
        self.__list = Cartitem_lst
        self.__address = Address
        self.__Status = Status
        self.__TotalAmount = TotalAmount
        Order.order_id += 1
    
    def get_id(self):
        return self.__id
    
    def update_status(self, massage):
        self.__Status = massage
        return True
    
    def __str__(self):
        return f'{self.__id}  {self.__list} {self.__address} {self.__Status} {self.__TotalAmount} '

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

class Address:
    def __init__(self, name ,addr , city, post_code, phone):
        self.__name = name
        self.__addr = addr
        self.__city = city
        self.__post_code = post_code
        self.__phone_number = phone