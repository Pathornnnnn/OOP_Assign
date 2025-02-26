from fasthtml.common import *
from create_instance import *
from css import *
import os
OrangeIT = create_instance()
app, rt = fast_app()


UPLOAD_DIR = "PIC"
os.makedirs(UPLOAD_DIR, exist_ok=True)
# PATH

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
        Div(id="results", cls="product-container", *[
            Div(
                Img(src=product.get_img(), alt=product.get_name()),
                H3(product.get_name()),
                P(f"Price : {product.get_price()} THB"),
                cls="product-card"
            ) for product in OrangeIT.get_lst_product()
        ]),Div(
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
@rt('/p')
def get():
    return Body(H1('Enter parameter after /p/...'))

@rt('/p/Monitor')
def get():
    return Titled(
        "Banana : Select Item Page",
        Div(
            Container(
                P("DELL P2425H 23.8 INCH IPS FHD 100HZ 5MS *จอคอมพิวเตอร์"),
                Grid(
                    Img(src="https://storage.googleapis.com/file-computeandmore/large_images/3627867c-c3b1-4db0-b9eb-27b9a4b15ffe.png",style="width: 300px; height: 300px;", alt="ตัวอย่างภาพ"),
                    style="text-align: center; background-color:rgb(182, 255, 253);"
                ),
                Container(
                    Grid(
                        
                        Div(P("ทำงานได้อย่างมีประสิทธิภาพ รับความสบายตาที่เพิ่มมากขึ้นและการเชื่อมต่อที่ราบรื่นด้วยจอภาพ FHD ที่ได้รับการรับรองจาก TÜV ว่าสบายตาในระดับ 4 ดาวจุดเด่นสินค้าลดการปล่อยแสงสีฟ้าอันเป็นอันตรายเหลือ ≤35% เพื่อความสบายตลอดทั้งวันโดยไม่ต้องเสียสละสีสันอัตราการรีเฟรช 100Hz ช่วยลดการสั่นไหว เลื่อนภาพได้ลื่นไหลยิ่งขึ้น และเคลื่อนไหวได้ราบรื่นยิ่งขึ้นครอบคลุมสีที่กว้างโดยมีสีที่แสดงได้สูงสุดถึง 16.7 ล้านสีที่ 99% sRGBสีสันสดใสในมุมมองที่กว้างด้วยเทคโนโลยี In-Plane Switching (IPS)"), cls="box")
                    ),
                    Button("Add Cart",style="margin-right: 20px; text-align: center;"),Button("Purchase",style="text-align: center;"),
                    style="text-align: center; background-color:rgb(94, 93, 93);"
                )     
            )
        )

    )

@rt('/p/Keyboard')
def get():
    return Titled(
        "Banana : Select Item Page",
        Div(
            Container(
                P("คีย์บอร์ดเกมมิ่ง Signo Gaming Keyboard Nuzzon KB-751 Wireless Mechanical Black (Blue Switch)"),
                Grid(
                    Img(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp7b8xCcf89FHFziDHJ8Asl1k3dHk49AlMgA&s",style="width: 300px; height: 300px;", alt="ตัวอย่างภาพ"),
                    style="text-align: center; background-color:rgb(182, 255, 253);"
                ),
                Container(
                    Grid(
                        
                        Div(P("KB 751 NUZZON PUDDING WIRELESS OPTICAL SWITCH KEYBOARD การส่งคำสั่งและการตอบสนองที่เร็วกว่าเพียง 2 MS ทำงานด้วยระบบ INFARED ตอบสนองได้เร็วกว่า มีความทนทานและแก้ปัญหาปุ่มเบิ้ล รองรับการกดได้มากถึง 100 ล้านครั้ง  ใช้งานได้นานสูงสุด 20 ชม. ( แบบปิดไฟ ) 10 ชม. (แบบเปิดไฟ) วัสดุเป็นพลาสติก ABS แข็งแรง ทนทาน  มีฟังค์ชั่นล็อควินโดว์ ปุ่มคีย์บอร์ดแบบจมเพิ่มความเรียบหรู พร้อมอะแดปเตอร์ขยายตัวรับสัญญาน"), cls="box")
                    ),
                    Button("Add Cart",style="margin-right: 20px; text-align: center;"),Button("Purchase",style="text-align: center;"),
                    style="text-align: center; background-color:rgb(94, 93, 93);"
                )     
            )
        )

    )



#cart
@rt('/cart')
def get():
    pass



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