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
account_now = None
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

@rt("/loginCheck")
def post(email: str, password: str):
    global account_now
    acc = OrangeIT.check_login(email, password)
    if acc:
        print(f"✅ Login Success: {acc}")
        account_now = acc
        return Redirect("/")  # กลับไปหน้าแรกถ้า Login สำเร็จ
    return "❌ Login Failed! กรุณาตรวจสอบอีเมลหรือรหัสผ่าน", 401  # แจ้งเตือนถ้าข้อมูลผิด


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
                A(Div(
                    Img(src="https://cdn-icons-png.flaticon.com/128/1077/1077063.png", cls="icon"),
                    cls="login"
                ),href= '/login'),
                A(
                    Div(
                    Img(src="https://cdn-icons-png.flaticon.com/128/5392/5392794.png", cls="icon cart"),
                    cls="header-buttons"
                , href='/register'))
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

serve()



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

#cart
@rt('/cart/{product_id}')   
def post(product_id: int , quantity: int=1):
    global account_now
    print(product_id,quantity,account_now)

    try:
        quantity = int(quantity)
        if quantity <= 0:
            return Div(P("❌ Invalid quantity!", cls="error"))
    except ValueError:
        return Div(P("❌ Invalid quantity format!", cls="error"))

    if not account_now or not isinstance(account_now, Customer):
        return Div(P("account Not Found", cls="error"))
    else:
        account_id = account_now.get_id()
        OrangeIT.add_to_cart(product_id,quantity,account_id)
        print('ID :',account_now.get_id(),'| Name :',  account_now.get_name() ,'| Cart :', account_now.get_cart_shopping())
        return Div(P("Add cart", cls="error"))




#checkout
@rt('/checkout')
def get():
    pass



#payment
@rt('/payment')
def get():
    pass



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