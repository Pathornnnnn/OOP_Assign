from fasthtml.common import *
from create_instance import create_instance
from OrangeIT import *
from css import *
import os
import shutil
app, rt = fast_app()
OrangeIT = create_instance()
#print([[i.get_id() , i.get_name()]for i in OrangeIT.get_product_lst()])
UPLOAD_DIR = "PIC"
UPLOAD_DIR2 = "p/PIC"
os.makedirs(UPLOAD_DIR, exist_ok=True)
# PATH
global account_now
global tem_address
global discount
account_now = None #<----- ที่จริงต้องเก็บเป็น string
order_id = None
discount = 0
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
        if not OrangeIT.verify_admin(account_now):
            return Redirect("/")  # กลับไปหน้าแรกถ้า Login สำเร็จ
        else:
            return Redirect("/admin_home")
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
                action='/add_acc', method='post',
                _class='register-form'
            ),
            _class='register-container',style="align-items: center;"
        ),
        Style(login_css)
    )

@rt('/add_acc')
def post(Fullname : str, email : str , password  :str , age :int):
    try:
        OrangeIT.register(Fullname, email, password , age)
        return Redirect('/login')
    except:
        return False

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


@rt('/admin_home')
def get():
    return Html(
        Body(
            Div(
                H1("📌 Admin Dashboard", cls="admin-header"),
                Div(
                    A(Button("✅ ตรวจสอบคำสั่งซื้อ", cls="admin-btn"), href="/verify_order"),
                    A(Button("➕ เพิ่มสินค้า", cls="admin-btn"), href="/add_product"),
                    A(Button("จัดการสินค้า", cls="admin-btn"), href="/manage_product"),
                    cls="admin-menu"
                ),
                id="admin-home"
            )
        )
    ),Style(admin_home_css)

@rt('/approve_order/{order}')
def post(order : int):
    print('apporve')
    OrangeIT.change_status_order_by_id(order, "Accept Order (wait for shipping)")
    return Redirect('/verify_order')

@rt('/reject_order/{order_id}')
def post(order_id : int):
    print('reject')
    OrangeIT.change_status_order_by_id(order_id, "Reject Order")
    return Redirect('/verify_order')


@rt('/verify_order')
def get():
    if not OrangeIT.verify_admin(account_now):
        print('you not admin bye')
        return Div(P("account Not Found", cls="error"))
    else:
        orders = OrangeIT.get_pending_orders()  # ดึงคำสั่งซื้อที่รอการตรวจสอบ
        return Html(
            Body(
                Div(
                    H1("✅ ตรวจสอบคำสั่งซื้อ", cls="verify-header"),
                    Table(
                        Tr(Th("Order ID"), Th("สินค้า"), Th("ที่อยู่"), Th("ยอดรวม"), Th("ดำเนินการ")),
                        *[
                            Tr(
                                Td(order.get_id()),
                                Td(
                                    Ul(
                                        *[Li(item.get_product().get_name()) for item in order.get_list()]
                                    ),
                                    cls="order-items"
                                ),
                                Td(order.get_address(), cls="order-address"),
                                Td(f"฿{order.get_total_amount()}", cls="order-total"),
                                Td(
                                    Form(
                                        Button("✅ อนุมัติ", type="submit", cls="approve-btn"),
                                        action=f"/approve_order/{order.get_id()}",
                                        method="post",
                                        hx_post=f"/approve_order/{order.get_id()}",
                                        hx_target="closest tr"
                                    ),
                                    Form(
                                        Button("❌ ปฏิเสธ", type="submit", cls="reject-btn"),
                                        action=f"/reject_order/{order.get_id()}",
                                        method="post",
                                        hx_post=f"/reject_order/{order.get_id()}",
                                        hx_target="closest tr"
                                    )
                                )
                            )
                            for order in orders
                        ],
                        cls="order-table"
                    ),
                    id="verify-orders"
                )
            )
        ),Style(verify_order)

@rt('/delete_product/{product_id}')
def post(product_id: int):
    print('delete product')
    OrangeIT.delete_product_by_id(product_id)
    return Redirect('/manage_product')

@rt('/manage_product')
def get():
    if not OrangeIT.verify_admin(account_now):
        return Div(P("Access Denied", cls="error"))
    
    products = OrangeIT.get_product_lst()  # ดึงข้อมูลสินค้าทั้งหมด
    
    return Html(
        Body(
            Div(
                H1("🛍️ จัดการสินค้า", cls="manage-header"),
                
                Form(
                        Button("➕ เพิ่มสินค้า", cls="add-btn", hx_target="body"),
                        action=f"/add_product",
                        method="get"
                    ),
                Table(
                    Tr(Th("รหัสสินค้า"), Th("ชื่อสินค้า"), Th("ราคา"), Th("สต็อก"), Th("การจัดการ")),
                    *[
                        Tr(
                            Td(product.get_id()),
                            Td(product.get_name()),
                            Td(f"฿{product.get_price()}"),
                            Td(product.get_stock()),
                            Td(
                                Form(
                                    Button("✏️ แก้ไข", type="submit", cls="edit-btn"),
                                    action=f"/edit_product/{product.get_id()}",
                                    method="post"
                                ),
                                Form(
                                    Button("🗑️ ลบ", type="submit", cls="delete-btn"),
                                    action=f"/delete_product/{product.get_id()}",
                                    method="post"
                                )
                            )
                        )
                        for product in products
                    ],
                    cls="product-table"
                ),
                id="manage-products"
            )
        )
    ),Style(manage_product_css)


@rt('/edit_product/{product_id}')
def post(product_id: int):
    if not OrangeIT.verify_admin(account_now):
        return Div(P("คุณไม่มีสิทธิ์เข้าถึง", cls="error"))

    product = OrangeIT.search_product_by_id(product_id)
    if not product:
        return Div(P("ไม่พบสินค้า", cls="error"))

    return Html(
        Body(
            Div(
                H1("✏️ แก้ไขสินค้า", cls="edit-header"),
                Form(
                    Label("ชื่อสินค้า:"),
                    Input(type="text", name="name", value=product.get_name(), required=True),
                    Label("ราคา (บาท):"),
                    Input(type="number", name="price", value=product.get_price(), required=True, step="0.01"),
                    Label("สต็อก:"),
                    Input(type="number", name="stock", value=product.get_stock(), required=True),
                    Input(type="hidden", name="product_id", value=product_id),  # ซ่อน product_id ไว้
                    Button("💾 บันทึก", type="submit", cls="save-btn"),
                    cls="edit-form",
                    method="post",  # ✅ กำหนด method POST
                    action="/update_product"  # ✅ ส่งข้อมูลไปที่ /update_product
                ),
                id="edit-product"
            )
        )
    ),Style(edit_product_css)



@rt('/add_product')
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
    try:
        # Ensure the directories exist
        if not os.path.exists(UPLOAD_DIR):
            os.makedirs(UPLOAD_DIR)
        if not os.path.exists(UPLOAD_DIR2):
            os.makedirs(UPLOAD_DIR2)
        
        # Save the file to the first path (UPLOAD_DIR)
        file_path = os.path.join(UPLOAD_DIR, img.filename)
        with open(file_path, "wb") as f:
            f.write(img.file.read())

        # Save the file to the second path (UPLOAD_DIR2)
        file_path2 = os.path.join(UPLOAD_DIR2, img.filename)
        shutil.copy(file_path, file_path2)
        
        # Create the product and add it
        relative_path = f"{UPLOAD_DIR}/{img.filename}"
        product = Product(name, price, description, description, relative_path)
        OrangeIT.add_product(product)

        # Return the HTML div structure with the product details
        return Div(
            Img(src=product.get_img(), alt=product.get_name()),
            H3(product.get_name()),
            P(f"Price : {product.get_price()} THB"),
            cls="product-card"
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@rt('/update_product')
def post(name : str , price: int , stock : int , product_id : int):
    OrangeIT.update_product(product_id, name, price, stock)
    return Redirect('/manage_product')


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
    
@rt('/p/{id}')
def get(id: int):
    product = OrangeIT.search_product_by_id(id)
    if not product:
        return Div(P("Product Not Found", cls="error"))

    reviews = OrangeIT.get_reviews_by_product_id(id)  # ดึงรีวิวของสินค้านี้

    return Style(product_css), Div(
        Div(A(H1("ORANGE", cls="header-title"), href='/'), cls="header-container"),
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
                    Input(type="number", name="quantity", value="1", min="1", max=f'{product.get_stock()}'),
                    Div(
                        Form(
                            Button("ซื้อเลย", cls="buy-btn", style='margin-right:5px', hx_post=f'/purchase/{product.get_id()}')
                        ),
                        Form(
                            Button("เพิ่มลงตะกร้า", cls="buy-btn", type="submit", style="background-color:gray;"),
                            hx_post=f'/cart/{product.get_id()}',
                            hx_include="[name='quantity']", 
                            hx_target="body",
                        ),
                    ),
                    Button("⭐ รีวิวสินค้า", cls="review-btn", hx_get=f"/review_form/{id}", hx_target="#review-form-container", hx_swap="innerHTML"),
                    Div(id="review-form-container"),  # ที่ว่างให้โหลดฟอร์มรีวิว
                    cls="product-info"
                ),
                cls="product-detail-container"
            ),
            cls="container"
        ),
        Div(
            H3("📝 รีวิวสินค้า", cls="review-title"),
            Div(
                *[
                    Div(
                        P(f"{review.get_user_name()} ให้คะแนน: {'⭐' * review.get_rating()}", cls="review-rating"),
                        P(review.get_comment(), cls="review-text"),
                        cls="review"
                    )
                    for review in reviews
                ], 
                id="review-list"
            ),
            cls="review-container"
        ),
        Div(P("© 2025 OrAnGe Store | All Rights Reserved.", cls="footer"), cls="container")
    )

@rt('/review_form/{id}')
def get(id: int):
    return Div(
        Form(
            Label("ให้คะแนนสินค้า:", cls="review-label"),
            Select(
                *[Option(f"{i} ดาว", value=i) for i in range(1, 6)],
                name="rating",
                cls="review-rating-select"
            ),
            Label("แสดงความคิดเห็น:", cls="review-label"),
            Textarea(name="review_text", placeholder="พิมพ์รีวิวของคุณที่นี่...", cls="review-textarea"),
            Button("ส่งรีวิว", cls="submit-review-btn", type="submit", hx_post=f"/submit_review/{id}", hx_target="#review-list", hx_swap="beforeend"),
            cls="review-form"
        )
    )

@rt('/submit_review/{id}')
def post(id: int, rating: int, review_text: str):
    user = OrangeIT.search_acc_by_id(account_now)
    if not user:
        return P("กรุณาเข้าสู่ระบบก่อนรีวิว", cls="error")

    OrangeIT.add_review(account_now ,id , rating, review_text)  # บันทึกรีวิวลงระบบ
    return Div(
        P(f"{user.get_name()} ให้คะแนน: {'⭐' * rating}", cls="review-rating"),
        P(review_text, cls="review-text"),
        cls="review"
    )


@rt('/purchase/{product_id}')
def post(product_id : int):
    global account_now
    if not account_now:
        return Div(P("account Not Found", cls="error"))
    else:
        OrangeIT.add_to_cart(product_id,1,account_now)
        #print result
        temp_acc = OrangeIT.search_acc_by_id(account_now)
        print('ID :',temp_acc.get_id(),'| Name :',  temp_acc.get_name() ,'| Cart :', temp_acc.get_cart_shopping())

        return Redirect("/view_cart")

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
    
#view_cart
@rt('/view_cart')
def get():
    if not account_now:
        return Div(P("account Not Found", cls="error"))
    
    temp_acc = OrangeIT.search_acc_by_id(account_now)
    cart = temp_acc.get_cart_shopping()
    total_price = cart.get_price_total()
    cart_items = cart.get_cart_lst()
    total_quantity = sum(item.get_quantity() for item in cart_items)

    return Div(
        H1(f'🛒 ตะกร้าสินค้า ({total_quantity})', cls='cart-header'),
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
        ) if total_quantity > 0 else P("❌ ตะกร้าสินค้าว่าง กรุณาเลือกสินค้าก่อนทำการสั่งซื้อ", cls="cart-empty-msg"),
        P(f"ยอดรวม: ฿{total_price}", cls="total-price"),
        Form(Button("ดำเนินการสั่งซื้อ", cls="checkout-btn", type="submit", disabled=(total_quantity == 0)), action="/checkout"),
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

@rt('/checkout')
def checkout():
    print(account_now)
    if not account_now:
        return Div(P("Account Not Found", cls="error"))

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
            Div(P(f"Total: ฿{total_price}", cls="total-price", id="total_prices")),  # ใช้ ID เพื่ออัปเดต
            
            # ฟอร์มที่อยู่ + คูปอง
            Form(
                H3("Shipping Address"),
                Div(Label("Full Name"), Input(type="text", id="full_name", required=True, placeholder="Enter your full name", cls="input-field")),
                Div(Label("Address"), Input(type="text", id="address", required=True, placeholder="Enter your address", cls="input-field")),
                Div(Label("City"), Input(type="text", id="city", required=True, placeholder="Enter your city", cls="input-field")),
                Div(Label("Postal Code"), Input(type="text", id="postal_code", required=True, placeholder="Enter postal code", cls="input-field")),
                Div(Label("Phone Number"), Input(type="tel", id="phone", required=True, placeholder="Enter phone number", cls="input-field")),
                
                # ✅ ปุ่มใช้คูปอง
                Div(
                    Label("Coupon"),
                    Input(type="text", id="coupon", placeholder="Enter coupon code", cls="input-field"),
                    Button("Use Code", hx_post="/use_coupon/", hx_target="#total_prices", hx_include="[name='coupon']", cls="coupon-btn")
                ),
                
                Button("Proceed to Payment", cls="checkout-btn", hx_post="/payment", hx_target="body"),
                cls="checkout-container"
            ),
        ),
        Div(P("© 2025 OrAnGe Store | All Rights Reserved.", cls="footer"), cls="container")
    )

@rt('/use_coupon/')
def apply_coupon(coupon: str):
    global discount
    print('Code :',coupon)
    temp_acc = OrangeIT.search_acc_by_id(account_now)
    
    if not temp_acc:
        return P("❌ Error: Account not found", cls="error")

    total_price = temp_acc.get_cart_shopping().get_price_total()
    discount = OrangeIT.search_coupon_by_code(coupon)  # ตรวจสอบคูปอง

    if discount > 0:  
        new_total = total_price - discount  # หักส่วนลด
        return P(f"🎉 คุณได้รับส่วนลด {discount} บาท Total: ฿{new_total:.2f}", cls="total-price")
    else:
        return P("❌ คูปองไม่ถูกต้อง", cls="error")


#payment    
@rt('/payment')
def post(full_name:str , address: str , city : str , postal_code: str , phone: str ):
    global order_id
    global discount
    if not account_now:
        return Div(P("account Not Found", cls="error"))
    acc = OrangeIT.search_acc_by_id(account_now)
    for i in acc.get_myorder_lst():
        print(i)
    order_id = OrangeIT.creat_order_acc(account_now, full_name, address, city, postal_code ,phone , discount)
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
                            Td(order.get_status(), cls="order-status"),
                            Td(order.get_address(), cls="order-address"),
                            Td(f"฿{order.get_total_amount()}", cls="order-total"),
                            Td(Button("🔍", cls="view-btn", hx_post=f"/order_details/{order.get_id()}", hx_target="#order-details-container", hx_swap="innerHTML"))
                        )
                        for order in orders
                    ],
                    cls="order-table"
                ),
                Div(id="order-details-container", cls="order-details-container"),
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
        P(f"สถานะ: {order.get_status()}", cls="order-status"),
        P(f"ที่อยู่จัดส่ง: {order.get_address()}", cls="order-address"),
        P(f"ยอดรวม: ฿{order.get_total_amount()}", cls="order-total"),
        H3("รายการสินค้า", cls="order-items-header"),
        Ul(
            *[Li(f"{item.get_product().get_name()} - {item.get_quantity()} ชิ้น (฿{item.get_price_product() * item.get_quantity()})") for item in order.get_list()]
        ),
        Button(
                    "ปิด",
                    cls="close-btn",
                    hx_post="/clear_order_details",
                    hx_target="#order-details-container",
                    hx_swap="innerHTML"
                )

    ),Style(view_order)

@rt('/clear_order_details')
def post():
    return ""
serve()