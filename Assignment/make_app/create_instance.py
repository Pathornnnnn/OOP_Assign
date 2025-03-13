from .class_orangeit import *

def create_instance():
    #init usr

    maxkey = Customer('MAX','MAX@gmail.com','111',11)
    jj = Customer('JJ','JJ@gmail.com','2222',32)
    admin1 = Admin('Gold','admin@gmail.com','1234',25)

    admin_lst = []
    admin_lst.append(admin1)

    user_lst = []
    user_lst.append(maxkey)
    user_lst.append(jj)

    #init product
    product1 = Product("Apple iPhone 13 128GB Midnight", 17200, "qwe", 5, "PIC\Apple iPhone 13 128GB Midnight.png")
    product2 = Product("Apple iPhone 16e 128GB Black", 22900, "qwe", 5, "PIC\Apple iPhone 16e 128GB Black.png")
    product3 = Product("Apple iPhone 16e 128GB White", 22900, "qwe", 5, "PIC\Apple iPhone 16e 128GB White.png")
    product4 = Product("ร่ม Jisulife FA52 Portal Umbrella Fan Pink", 1190 ,"qwe", 5, "PIC\ร่ม Jisulife FA52 Portal Umbrella Fan Pink.png")
    product5 = Product("Apple iPhone 16 Pro Max 256GB Desert Titanium", 46400,"qwe", 5, "PIC\Apple iPhone 16 Pro Max 256GB Desert Titanium.png")
    product6 = Product("Apple Watch Series 10 GPS 42mm Rose Gold Aluminium Case with Light Blush Sport Band - S/M", 13300, "qwe", 5,"PIC\Apple Watch Series 10 GPS 42mm Rose Gold Aluminium Case with Light Blush Sport Band.png")
    product7 = Product("Apple iPad Mini 7 (2024) Wi-Fi 256GB 8.3 inch Blue", 21900, "qwe", 5,"PIC\Apple iPad Mini 7 (2024) Wi-Fi 256GB 8.3 inch Blue.png")
    product8 = Product("สมาร์ทโฟน Samsung Galaxy S25 (12+512) Silver Shadow (5G)", 34900, "qwe", 5,"PIC\สมาร์ทโฟน Samsung Galaxy S25 (12+512) Silver Shadow (5G).png")
    product9 = Product("Apple iPhone 16",28700,"qwe", 5,"PIC\9.png")
    product10 = Product("Apple iPhone 16 Plus",34400,"qwe", 5,"PIC\Apple iPhone 16 Plus.png")
    product11 = Product("Apple iPad mini 7 (A17 Pro) Wi-Fi 8.3 inch",17900,"qwe", 5,"PIC/Apple iPad mini 7.png")
    product12 = Product("Apple iPad Air 5 Wi-Fi + Cellular 10.9 inch 2022",20900,"qwe", 5,"PIC/12.png")
    product13 = Product("Apple MacBook Pro 14 M4 chip",54900,"qwe", 5,"PIC/13.png")
    product14 = Product("Apple iMac 24 M4 chip Nano-texture glass",58900,"qwe", 5,"PIC/14.png")
    product15 = Product("หูฟังไร้สาย Apple AirPods 4",4150,"qwe", 5,"PIC/15.png")
    product16 = Product("Apple AirPods Max - Purple",19900,"qwe", 5,"PIC/16.png")
    product17 = Product("หูฟังไร้สาย Beats Studio Buds Black",4500,"qwe", 5,"PIC/17.png")
    product18 = Product("Apple Watch Series 10 (42mm) Aluminium",13300,"qwe", 5,"PIC/18.png")
    product19 = Product("Apple Watch Series  9 (45mm) Aluminium",12200,"qwe", 5,"PIC/19.png")
    product20 = Product("Apple 20W USB-C Port Power Adapter",640,"qwe", 5,"PIC/20.png")
    product21 = Product("Apple USB-C to Lightning Cable (1m)",750,"qwe", 5,"PIC/21.png")


    product_lst = []
    product_lst.append(product1)
    product_lst.append(product2)
    product_lst.append(product3)
    product_lst.append(product4)
    product_lst.append(product5)
    product_lst.append(product6)
    product_lst.append(product7)
    product_lst.append(product8)
    product_lst.append(product9)
    product_lst.append(product10)
    product_lst.append(product11)
    product_lst.append(product12)
    product_lst.append(product13)
    product_lst.append(product14)
    product_lst.append(product15)
    product_lst.append(product16)
    product_lst.append(product17)
    product_lst.append(product18)
    product_lst.append(product19)
    product_lst.append(product20)
    product_lst.append(product21)

    coupon_lst = []
    coupon1 = Coupon('XYZ','FREE1',1)
    coupon2 = Coupon('CEDT','DIS99',99)
    coupon_lst.append(coupon1)
    coupon_lst.append(coupon2)

    card_lst = []
    card1 = Card('1111222233334444','12/25','333',50000)
    card2 = Card('1111222233334444','12/25','444',500000)
    card_lst.append(card1)
    card_lst.append(card2)

    #init System
    OrangeIT = Controller(user_lst,product_lst,admin_lst,coupon_lst,[],card_lst)
    # TEST API
    # # เพิ่มสินค้า Monitor จำนวน 2 ชิ้น ลงตะกร้าของไอดี 1 (MAX)
    # OrangeIT.add_to_cart(1,2,1)
    # OrangeIT.add_to_cart(5,2,1)
    # เพิ่มสินค้า Monitor จำนวน 2 ชิ้น ลงตะกร้าของไอดี 1 (MAX)
    # acc = OrangeIT.search_acc_by_id(1)
    # print('ID :',acc.get_acc_id(),'| Name :',  acc.get_name() ,'| Cart :', acc.get_cart_shopping())
    # print('ID :',jj.get_acc_id(),'| Name :',  jj.get_name() ,'| Cart :', jj.get_cart_shopping())

    return OrangeIT