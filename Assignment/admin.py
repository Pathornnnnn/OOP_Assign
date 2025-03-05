from fasthtml.common import *
from css import *
from main import *

print(rt)
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

