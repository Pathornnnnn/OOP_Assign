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
                        A  (
                            Div(
                                    P(f'{acc_name} , Click to logout',cls="login"),
                                    Img(src="https://cdn-icons-png.flaticon.com/128/1077/1077063.png", cls="icon"),
                                    cls="login"
                                )   ,href= '/logout'
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

        return Div(P("Add cart", cls="error"))
#iei
#view_cart
@rt('/view_cart')
def get():
    if not account_now or not isinstance(account_now, Customer):
        return Div(P("Account Not Found", cls="error"))
    
    cart_items = account_now.get_cart_shopping().get_cart_lst()
    total_price = sum(item.get_product().get_price() * item.get_quantity() for item in cart_items)

    return Div(
        H1(f'🛒 ตะกร้าสินค้า ({sum(item.get_quantity() for item in cart_items)})', cls='cart-header'),
        Table(
            Tr(Th("สินค้า"), Th("จำนวน"), Th("ราคา"), Th("ลบ")),
            *[
                Tr(
                    Td(item.get_product().get_name()),
                    Td(
                        Div(
                            Button("-", cls="qty-btn", hx_post=f"/update_cart/{item.get_product().get_id()}/decrease", hx_target="#cart"),
                            Span(item["quantity"], cls="qty-span"),
                            Button("+", cls="qty-btn", hx_post=f"/update_cart/{item.get_product().get_id()}/increase", hx_target="#cart"),
                            cls="qty-container"
                        )
                    ),
                    Td(f"฿{item['price'] * item['quantity']}"),
                    Td(Button("❌", cls="delete-btn", hx_post=f"/remove_cart/{item['id']}", hx_target="#cart"))
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
    if not account_now or not isinstance(account_now, Customer):
        return Div(P("Account Not Found", cls="error"))
    
    if action == "increase":
        OrangeIT.update_cart_quantity(account_now.get_id(), product_id, 1)
    elif action == "decrease":
        OrangeIT.update_cart_quantity(account_now.get_id(), product_id, -1)

    return get()  

@rt('/remove_cart/{product_id}')
def post(product_id: int):
    if not account_now or not isinstance(account_now, Customer):
        return Div(P("Account Not Found", cls="error"))
    
    OrangeIT.remove_from_cart(account_now.get_id(), product_id)
    return get()  

#checkout
@rt('/checkout')
def checkout():
    if not account_now or not isinstance(account_now, Customer):
        return Div(P("account Not Found", cls="error"))
    
    cartitems_lst = account_now.get_cart_shopping().get_cart_lst()
    total_price = account_now.get_cart_shopping().get_price_total()
    
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
                    Input(type="text", name="full_name", required=True, placeholder="Enter your full name", cls="input-field")
                ),
                Div(
                    Label("Address"),
                    Input(type="text", name="address", required=True, placeholder="Enter your address", cls="input-field")
                ),
                Div(
                    Label("City"),
                    Input(type="text", name="city", required=True, placeholder="Enter your city", cls="input-field")
                ),
                Div(
                    Label("Postal Code"),
                    Input(type="text", name="postal_code", required=True, placeholder="Enter postal code", cls="input-field")
                ),
                Div(
                    Label("Phone Number"),
                    Input(type="tel", name="phone", required=True, placeholder="Enter phone number", cls="input-field")
                ),
                
                Button("Proceed to Payment", cls="checkout-btn", hx_get='/payment', hx_target='body'),
                cls="checkout-container"
            ),
        ),
        Div(P("© 2025 OrAnGe Store | All Rights Reserved.", cls="footer"), cls="container")
    )

#payment    
@rt('/payment')
def payment():
    return Style(payment_css), Div(
        Div(A(H1("ORANGE", cls="header-title"), href='/'), cls="header-container"),
        Div(
            H2("💳 Payment"),
            Form(
                P("Card Number:"),
                Input(type="text", name="card_number", placeholder="xxxx-xxxx-xxxx-xxxx"),
                P("Expiry Date:"),
                Input(type="text", name="expiry_date", placeholder="MM/YY"),
                P("CVV:"),
                Input(type="text", name="cvv", placeholder="123"),
                Button("Pay Now", cls="pay-btn", hx_post='/confirm-payment', hx_target='body')
            ),
            cls="payment-container"
        ),
        Div(P("© 2025 OrAnGe Store | All Rights Reserved.", cls="footer"), cls="container")
    )

#my_order
@rt('/my_order')
def get():
    pass

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

serve()