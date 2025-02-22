from OrangeIT import *
def create_instance():
    #init usr

    maxkey = Customer("1",'MAX','MAX@gmail.com')
    jj = Customer("2",'JJ','JJ@gmail.com')

    user_lst = []
    user_lst.append(maxkey)
    user_lst.append(jj)

    #init product
    monitor = Product(1,'Monitor')
    keyboard = Product(2,'Keyboard')

    product_lst = []
    product_lst.append(monitor)
    product_lst.append(keyboard)

    #init System
    OrangeIT = Controller(user_lst,product_lst)

    # TEST API
    # เพิ่มสินค้า Monitor จำนวน 2 ชิ้น ลงตะกร้าของไอดี 1 (MAX)
    OrangeIT.add_cart('Monitor',2,'1')
    # เพิ่มสินค้า Monitor จำนวน 2 ชิ้น ลงตะกร้าของไอดี 1 (MAX)
    OrangeIT.add_cart('Keyboard',5,'1')

        
    print('ID :',maxkey.get_acc_id(),'| Name :',  maxkey.get_name() ,'| Cart :', maxkey.get_cart_shopping())
    print('ID :',jj.get_acc_id(),'| Name :',  jj.get_name() ,'| Cart :', jj.get_cart_shopping())

    return OrangeIT