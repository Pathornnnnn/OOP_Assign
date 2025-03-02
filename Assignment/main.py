from fasthtml.common import *
from create_instance import create_instance
from OrangeIT import *
from css import *
import os

app, rt = fast_app()
OrangeIT = create_instance()
#print([[i.get_id() , i.get_name()]for i in OrangeIT.get_product_lst()])
UPLOAD_DIR = "PIC"
os.makedirs(UPLOAD_DIR, exist_ok=True)
# PATH
global account_now
global tem_address
account_now = None #<----- ที่จริงต้องเก็บเป็น string
order_id = None
#/login
@rt("/login")
def get():
    return Head(Div(Style(home_css), Div(

            A(H1("OrAnGeIT", cls="header-title"),href='/'),  # โลโก้ใหญ่ขึ้น
            cls="header-container",

    )),
        H2('Login', _class='login-title'),
        Div(
            Form(
                Input(type='email', name='email', placeholder='อีเมล', required=True),
                Input(type='password', name='password', placeholder='รหัสผ่าน', required=True),
                Button('Login', type='submit', _class='signup-btn'),
                action='/loginCheck', method='post', 
                _class='login-form'
            ),A(Button('Register', _class='register-btn'),href='/register'),
            _class='signup-container'
        ),
        Style(login_css)   
    )

#check
@rt("/loginCheck")
def post(email: str, password: str):
    global account_now
    acc = OrangeIT.check_login(email, password)
    if acc:
        print(f"✅ Login Success: {acc}")
        account_now = acc.get_acc_id()
        return Redirect("/")  # กลับไปหน้าแรกถ้า Login สำเร็จ
    return "❌ Login Failed! กรุณาตรวจสอบอีเมลหรือรหัสผ่าน", 401  # แจ้งเตือนถ้าข้อมูลผิด

#logout
@rt('/logout')
def get():
    global account_now
    account_now = None
    return Redirect("/")

#/register
@rt("/register")
def get():
    return Head(Div(Style(home_css), Div(

            A(H1("OrAnGeIT", cls="header-title"),href='/'),  # โลโก้ใหญ่ขึ้น
            cls="header-container",

    )),
        H2('Register', _class='register-title'),
        Div(Style(register_css),
            Form(
                Input(Id='Fullname', type='text', name='Fullname', placeholder='Fullname', required=True),
                Input(Id='email', type='email', name='email', placeholder='E-mail', required=True),
                Input(Id='password', type='password', name='password', placeholder='password', required=True),
                Input(Id='age', type='number', name='age', min='18', max='100',placeholder='Age'),
                Button('Register', type='submit', _class='register-btn'),
                action='/add', method='post',
                _class='register-form'
            ),
            _class='register-container',style="align-items: center;"
        ),
        Style(register_css)
    )

#/home
@rt('/')
def get():
    if account_now == None:
        return  Style(home_css),Div(
            Div(
                H1("OrAnGeIT", cls="header-title"),  # โลโก้ใหญ่ขึ้น
                Div(
                    Form(
                        Div(
                            Input(id="name", placeholder="ค้นหาสินค้าที่ต้องการที่นี่...", 
                                cls="search-input", hx_get="/search", 
                                target_id="results", hx_trigger="keyup delay:500ms"),
                            Button(cls="search-btn"),
                            cls="search-container"
                        )
                    ),
                ),
                Div(
                    Grid(
                        A  (
                            Div(
                                    P('Login/Register',cls="login"),
                                    Img(src="https://cdn-icons-png.flaticon.com/128/1077/1077063.png", cls="icon"),
                                    cls="login"
                                )   ,href= '/login'
                            )
                        ),
                    Grid(
                        A   (  
                            Div(
                                    Img(src="https://cdn-icons-png.flaticon.com/128/5392/5392794.png", cls="icon cart"),
                                    P('Cart',style='margin-right:10px;',cls="cart"),
                                    cls="cart"
                                )   , href='/view_cart'

                            )
                        )   
                ),
                cls="header-container"
            ),
            Div(id="results", cls="product-container", *
                [
                    Div(
                        Img(src=product.get_img(), alt=product.get_name()),
                        H3(product.get_name()),
                        P(f"Price : {product.get_price()} THB"),
                        Form(
                            Button('See Detail' ,type='submit',style= 'background-color:orange;'),
                            action= f'/p/{product.get_id()}',method = 'get',), 
                        cls="product-card",id = product.get_id(),
                    ) 
                    for product in OrangeIT.get_lst_product()]), 
                    Div(
        Div(id="results", cls="product-container"),
        Div(P("© 2025 OrAnGe Store | All Rights Reserved. | 67015105, 67015155, 67015167", cls="footer")),
        cls="container"
        )
    )
    else:
        ins_acc = OrangeIT.search_acc_by_id(account_now)
        acc_name = ins_acc.get_acc_name()
        return  Style(home_css),Div(
            Div(
                H1("OrAnGeIT", cls="header-title"),  # โลโก้ใหญ่ขึ้น
                Div(
                    Form(
                        Div(
                            Input(id="name", placeholder="ค้นหาสินค้าที่ต้องการที่นี่...", 
                                cls="search-input", hx_get="/search", 
                                target_id="results", hx_trigger="keyup delay:500ms"),
                            Button(cls="search-btn"),
                            cls="search-container"
                        )
                    ),
                ),
                Div(
                    Grid(
                            Div(
                                    A(P(f'{acc_name} , Click to logout',cls="login"), hx_get='/logout'),
                                    A(Img(src="https://cdn-icons-png.flaticon.com/128/1077/1077063.png", cls="icon"), href='/view_myorder'),
                                    cls="login"
                                )
                        ),
                    Grid(
                        A   (  
                            Div(
                                    Img(src="https://cdn-icons-png.flaticon.com/128/5392/5392794.png", cls="icon cart"),
                                    P('Cart',style='margin-right:10px;',cls="cart"),
                                    cls="cart"
                                )   , href='/view_cart'

                            )
                        )   
                ),
                cls="header-container"
            ),
            Div(id="results", cls="product-container", *
                [
                    Div(
                        Img(src=product.get_img(), alt=product.get_name()),
                        H3(product.get_name()),
                        P(f"Price : {product.get_price()} THB"),
                        Form(
                            Button('See Detail' ,type='submit',style= 'background-color:orange;'),
                            action= f'/p/{product.get_id()}',method = 'get',), 
                        cls="product-card",id = product.get_id(),
                    ) 
                    for product in OrangeIT.get_lst_product()]), 
                    Div(
        Div(id="results", cls="product-container"),
        Div(P("© 2025 OrAnGe Store | All Rights Reserved. | 67015105, 67015155, 67015167", cls="footer")),
        cls="container"
        )
    )

#search
@rt('/search')
def get(name: str):
    results = OrangeIT.search(name)
    if results:
        return Div(cls=("product-container"), *[Div(
            Img(src=product.get_img(), alt=product.get_name()),
            H3(product.get_name()),
            P(f"Price : {product.get_price()} THB"),
            cls=("product-card")
        ) for product in results])
    else:
        return Div(P("Products Not Found."))

#Product
@rt('/p/{id}')
def get(id: int):
    product = OrangeIT.search_product_by_id(id)
    if not product:
        return Div(P("Product Not Found", cls="error"))
    
    return Style(product_css), Div(
        Div(A(H1("ORANGE", cls="header-title"),href='/'), cls="header-container"),
        Div(
            Div(
                Div(
                    Img(src=product.get_img(), alt=product.get_name(), cls="product-image"),
                    cls="product-image-container"
                ),
                Div(
                    H2(product.get_name()),
                    P(f"ราคา: {product.get_price()}"),
                    P(product.get_description()),
                    Input(type="number",name="quantity", value="1", min = "1" , max=f'{product.get_stock()}'),
                    Div(
                        
                        Form(
                            Button("ซื้อเลย", cls="buy-btn" ,style='margin-right:5px' , hx_post='/purchase')
                            ),

                        Form(
                                Button("เพิ่มลงตะกร้า", cls="buy-btn" ,type="submit",style="background-color:gray;"),
                                # ใช้ `hx-include` เพื่อให้ input ส่งค่าไปด้วย
                                hx_post=f'/cart/{product.get_id()}',
                                hx_include="[name='quantity']", 
                                hx_target='Body',
                            )
                        
                        )
                    ,
                    cls="product-info"
                ),
                cls="product-detail-container"
            ),
            cls="container"
        ),
        Div(P("© 2025 OrAnGe Store | All Rights Reserved.", cls="footer"), cls="container")
    )

#add_to_cart
@rt('/cart/{product_id}')   
def post(product_id: int , quantity: int=1):
    global account_now
    try:
        quantity = int(quantity)
        if quantity <= 0:
            return Div(P("❌ Invalid quantity!", cls="error"))
    except ValueError:
        return Div(P("❌ Invalid quantity format!", cls="error"))

    if not account_now:
        return Div(P("account Not Found", cls="error"))
    else:
        OrangeIT.add_to_cart(product_id,quantity,account_now)
        #print result
        temp_acc = OrangeIT.search_acc_by_id(account_now)
        print('ID :',temp_acc.get_id(),'| Name :',  temp_acc.get_name() ,'| Cart :', temp_acc.get_cart_shopping())

        return Redirect("/")
#iei
#view_cart
@rt('/view_cart')
def get():
    if not account_now:
        return Div(P("account Not Found", cls="error"))
    
    temp_acc = OrangeIT.search_acc_by_id(account_now)
    cart = temp_acc.get_cart_shopping()
    total_price = cart.get_price_total()
    cart_items = cart.get_cart_lst()
    return Div(
        H1(f'🛒 ตะกร้าสินค้า ({sum(item.get_quantity() for item in cart_items)})', cls='cart-header'),
        Table(
            Tr(Th("สินค้า"), Th("จำนวน"), Th("ราคา"), Th("ลบ")),
            *[
                Tr(
                    Td(item.get_product().get_name()),
                    Td(
                        Div(
                            Button("-", cls="qty-btn", hx_post=f"/update_cart/{item.get_id()}/decrease", hx_target="#cart"),
                            Span(item.get_quantity(), cls="qty-span"),
                            Button("+", cls="qty-btn", hx_post=f"/update_cart/{item.get_id()}/increase", hx_target="#cart"),
                            cls="qty-container"
                        )
                    ),
                    Td(f"฿{item.get_price_product() * item.get_quantity()}"),
                    Td(Button("❌", cls="delete-btn", hx_post=f"/remove_cart/{item.get_id()}", hx_target="#cart"))
                )
                for item in cart_items
            ],
            cls="cart-table"
        ),
        P(f"ยอดรวม: ฿{total_price}", cls="total-price"),
        Form(Button("ดำเนินการสั่งซื้อ", cls="checkout-btn", type="submit"), action="/checkout"),
        Style(view_cart_css),
        id="cart"
    )

@rt('/update_cart/{product_id}/{action}')
def post(product_id: int, action: str):
    if not account_now:
        return Div(P("account Not Found", cls="error"))
    
    if action == "increase":
        OrangeIT.update_cart_quantity(account_now, product_id, 1)
    elif action == "decrease":
        OrangeIT.update_cart_quantity(account_now, product_id, -1)

    return Redirect('/view_cart')

@rt('/remove_cart/{product_id}')
def post(product_id: int):
    if not account_now:
        return Div(P("account Not Found", cls="error"))
    
    OrangeIT.remove_cartitem_by_id(account_now, product_id)

    return Redirect('/view_cart')

#checkout
@rt('/checkout')
def checkout():
    print(account_now)
    if not account_now:
        return Div(P("account Not Found", cls="error"))
    
    temp_acc = OrangeIT.search_acc_by_id(account_now)
    cartitems_lst = temp_acc.get_cart_shopping().get_cart_lst()
    total_price = temp_acc.get_cart_shopping().get_price_total()
    return Style(checkout_css), Div(
        Div(A(H1("ORANGE", cls="header-title"), href='/'), cls="header-container"),
        Div(
            H2("🛒 Checkout"),
            Table(
                Tr(Th("Product"), Th("Quantity"), Th("Price")),
                *[Tr(Td(item.get_product().get_name()), Td(item.get_quantity()), Td(f"฿{item.get_product().get_price()}")) for item in cartitems_lst],
                cls="checkout-table"
            ),
            P(f"Total: ฿{total_price}", cls="total-price"),
            
            # ฟอร์มสำหรับกรอกที่อยู่
            Form(
                H3("Shipping Address"),
                Div(
                    Label("Full Name"),
                    Input(type="text", id="full_name", required=True, placeholder="Enter your full name", cls="input-field")
                ),
                Div(
                    Label("Address"),
                    Input(type="text", id="address", required=True, placeholder="Enter your address", cls="input-field")
                ),
                Div(
                    Label("City"),
                    Input(type="text", id="city", required=True, placeholder="Enter your city", cls="input-field")
                ),
                Div(
                    Label("Postal Code"),
                    Input(type="text", id="postal_code", required=True, placeholder="Enter postal code", cls="input-field")
                ),
                Div(
                    Label("Phone Number"),
                    Input(type="tel", id="phone", required=True, placeholder="Enter phone number", cls="input-field")
                ),
                
                Button("Proceed to Payment", cls="checkout-btn", hx_post='/payment', hx_target='body'),
                cls="checkout-container"
            ),
        ),
        Div(P("© 2025 OrAnGe Store | All Rights Reserved.", cls="footer"), cls="container")
    )


    

#payment    
@rt('/payment')
def post(full_name:str , address: str , city : str , postal_code: str , phone: str):
    global order_id
    if not account_now:
        return Div(P("account Not Found", cls="error"))
    acc = OrangeIT.search_acc_by_id(account_now)
    for i in acc.get_myorder_lst():
        print(i)
    order_id = OrangeIT.creat_order_acc(account_now, full_name, address, city, postal_code ,phone)
    for i in acc.get_myorder_lst():
        print(i)
    OrangeIT.clear_cart_account_by_id(account_now)
    return Style(payment_css), Div(
        Div(A(H1("ORANGE", cls="header-title"), href='/'), cls="header-container"),
        Div(
            H2("📷 Scan to Pay"),
            Div(
                Img(src='/PIC/QR.jpg', alt='QR Code for Payment', cls='qr-code', style="width:250px; height:250px; display:block; margin:0 auto;"),
                P("Scan the QR code above to complete your payment.", style="text-align:center; color:#666;"),
                Button('Click to Confirm payment', hx_get = '/confirm-payment') ,
                cls="qr-container"
            ),
            cls="payment-container"
        ),
        Div(P("© 2025 OrAnGe Store | All Rights Reserved.", cls="footer"), cls="container")
    )

@rt('/confirm-payment')
def get():
    OrangeIT.change_status_order(account_now, order_id , "Wait Verify")
    acc = OrangeIT.search_acc_by_id(account_now)
    for i in acc.get_myorder_lst():
        print(i)
    print(f'update status order {order_id} to wait admin')
    OrangeIT.clear_cart_account_by_id(account_now)
    return Redirect('/')

@rt('/add')
def get():
    return  Body(
                Div(
                    A(H1("ORANGE Admin Add", cls="header-title"), cls="header-container", href = '/')),
                    Form(
                        Input(id="name", placeholder="ชื่อสินค้า"),
                        Input(id="price", placeholder="ราคาสินค้า"),
                        Input(id="description", placeholder="รายละเอียดสินค้า"),
                        Input(id="quantity", placeholder="จำนวน"),
                        Input(type="file", id="img", name="img"),
                        Button("Add"),
                        hx_post="/add_product",
                        hx_target="#items",
                        hx_swap="beforeend",
                        enctype="multipart/form-data",
                                ),
                Div(id="items", cls="product-container", children=[
                    Div(
                        Img(src=p.get_img(), alt=p.get_name()),
                        H3(p.get_name()),
                        P(f"Price : {p.get_price()} THB"),
                        cls="product-card"
                    ) for p in OrangeIT.get_lst_product()
                ]),
                Div(P("© 2025 OrAnGe Store | All Rights Reserved.", cls="footer"), cls="footer"),Style(add_css)
            )

@rt('/add_product')
def post(name: str, price: str, description:str ,quantity:str ,img: UploadFile):
    file_path = os.path.join(UPLOAD_DIR, img.filename)
    with open(file_path, "wb") as f:
        f.write(img.file.read())
    relative_path = f"{UPLOAD_DIR}/{img.filename}"

    product = Product(name, price, description, description, relative_path)
    OrangeIT.add_product(product)
    
    return Div(
        Img(src=product.get_img(), alt=product.get_name()),
        H3(product.get_name()),
        P(f"Price : {product.get_price()} THB"),
        cls="product-card"
    )
@rt('/view_myorder')
def get():
    global account_now
    if not account_now:
        return Div(P("Account Not Found", cls="error"))
    
    acc = OrangeIT.search_acc_by_id(account_now)
    orders = acc.get_myorder_lst()
    
    
    return  Body(
            Div(
                H1(f'📦 คำสั่งซื้อของฉัน ({len(orders)})', cls='order-header'),
                Table(
                    Tr(Th("Order ID"), Th("สินค้า"), Th("สถานะ"), Th("ที่อยู่"), Th("ยอดรวม"), Th("รายละเอียด")),
                    *[
                        Tr(
                            Td(order.get_id()),
                            Td(
                                Ul(
                                    *[Li(item.get_product().get_name()) for item in order.get_list()]
                                ),
                                cls="order-items"
                            ),
                            Td(order.get_Status(), cls="order-status"),
                            Td(order.get_address(), cls="order-address"),
                            Td(f"฿{order.get_TotalAmount()}", cls="order-total"),
                            Td(Button("🔍", cls="view-btn", hx_post=f"/order_details/{order.get_id()}", hx_target="#order-details-container", hx_swap="innerHTML"))
                        )
                        for order in orders
                    ],
                    cls="order-table"
                ),
                Div(id="order-details-container", cls="order-details-container"),Style(view_cart_css),
                id="orders"
            ),Style(view_order)
        )

@rt('/order_details/{order_id}')
def post(order_id: int):
    global account_now
    if not account_now:
        return Div(P("Account Not Found", cls="error"))
    order = OrangeIT.search_order_by_id(account_now , order_id)
    if not order:
        return Div(P("Order not found", cls="error"))
    
    return Div(
        H2(f"รายละเอียดคำสั่งซื้อ #{order.get_id()}", cls="order-detail-header"),
        P(f"สถานะ: {order.get_Status()}", cls="order-status"),
        P(f"ที่อยู่จัดส่ง: {order.get_address()}", cls="order-address"),
        P(f"ยอดรวม: ฿{order.get_TotalAmount()}", cls="order-total"),
        H3("รายการสินค้า", cls="order-items-header"),
        Ul(
            *[Li(f"{item.get_product().get_name()} - {item.get_quantity()} ชิ้น (฿{item.get_price_product() * item.get_quantity()})") for item in order.get_list()]
        ),
        Button("ปิด", cls="close-btn", hx_on="click: this.closest('.order-details-container').innerHTML = ''")
    ),Style(view_order)

@rt('/verify')
def get():
    pass

serve()