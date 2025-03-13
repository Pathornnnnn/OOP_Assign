from app import *
from make_app.css import*
import config
@rt('/coupons')
def get():
    coupon_lst = OrangeIT.get_coupon_lst()
    return Style(coupon_css), Div(
        Div(A(H1("ORANGE", cls="header-title"), href='/'), cls="header-container"),
        
        Div(
            H2("🎉 รายการคูปองทั้งหมด"),
            Table(
                Thead(
                    Tr(
                        Th("รหัสคูปอง"), 
                        Th("ชื่อ"), 
                        Th("ส่วนลด"),
                        Th('หมดอายุ')
                    )
                ),
                Tbody(
                    *[Tr(Td(c.get_code()), Td(c.get_name()), Td(c.get_discount()),Td(c.get_expire())) for c in coupon_lst]
                ),
                cls="coupon-table"
            ),
            cls="coupon-section"
        ),

        Div(P("© 2025 OrAnGe Store | All Rights Reserved.", cls="footer"), cls="container")
    )
    
#view_cart
@rt('/view_cart')
def get():
    if not config.account_now:
        return Style(error_css),Div(P("account Not Found", cls="error-message"),cls="error-box")
    
    temp_acc = OrangeIT.search_acc_by_id(config.account_now)
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
    if not config.account_now:
        return Style(error_css),Div(P("account Not Found", cls="error-message"),cls="error-box")
    
    if action == "increase":
        OrangeIT.update_cart_quantity(config.account_now, product_id, 1)
    elif action == "decrease":
        OrangeIT.update_cart_quantity(config.account_now, product_id, -1)

    return Redirect('/view_cart')

@rt('/remove_cart/{product_id}')
def post(product_id: int):
    if not config.account_now:
        return Style(error_css),Div(P("account Not Found", cls="error-message"),cls="error-box")
    
    OrangeIT.remove_cartitem_by_id(config.account_now, product_id)

    return Redirect('/view_cart')

@rt('/checkout')
def checkout():
    if not config.account_now:
        return Style(error_css),Div(P("Account Not Found", cls="error-message"),cls="error-box")

    temp_acc = OrangeIT.search_acc_by_id(config.account_now)
    cartitems_lst = temp_acc.get_cart_shopping().get_cart_lst()
    total_price = temp_acc.get_cart_shopping().get_price_total()

    return Head(
        Div(Style(checkout_css), 
            Div(
                A(H1("OrAnGeIT", cls="header-title"), href='/'),  # โลโก้
                cls="header-container"
            )
        ),
        H2('Checkout', _class='checkout-title'),
        Div(
            Style(checkout_css),
            Form(
                H3("Shipping Address", _class="form-title"),
                Input(Id='full_name', type='text', name='full_name', placeholder='Full Name', required=True),
                Input(Id='address', type='text', name='address', placeholder='Address', required=True),
                Input(Id='city', type='text', name='city', placeholder='City', required=True),
                Input(Id='postal_code', type='text', name='postal_code', placeholder='Postal Code', required=True),
                Input(Id='phone', type='tel', name='phone', placeholder='Phone Number', required=True),

                # ✅ คูปอง
                Input(Id='coupon', type='text', name='coupon', placeholder='Coupon Code'),
                Button("Use Code", hx_post="/use_coupon/", hx_target="#total_prices", hx_include="[name='coupon']", _class="coupon-btn"),

                P(f"Total: ฿{total_price}", Id="total_prices", _class="total-price"),  # ✅ แสดงราคาทั้งหมด

                Button('Proceed to Payment', type='submit', _class='checkout-btn'),
                action='/payment', method='post',
                _class='checkout-form'
            ),
            _class='checkout-container', style="align-items: center;"
        ),
        Style(checkout_css)
    ),Style(checkout_css)


@rt('/use_coupon/')
def apply_coupon(coupon: str):
    global discount, coupon_code
    temp_acc = OrangeIT.search_acc_by_id(config.account_now)
    
    if not temp_acc:
        return Style(error_css),P("❌ Error: Account not found", cls="error-message")

    total_price = temp_acc.get_cart_shopping().get_price_total()
    discount = OrangeIT.search_coupon_by_code(coupon)  # ตรวจสอบคูปอง

    if discount != False:  
        coupon_code = coupon
        new_total = total_price - discount  # หักส่วนลด
        return P(f"🎉 คุณได้รับส่วนลด {discount} บาท Total: ฿{new_total:.2f}", cls="total-price")
    else:
        coupon_code = None
        return P("❌ คูปองไม่ถูกต้อง", cls="error-message")


#payment    
@rt('/payment')
def post(full_name:str , address: str , city : str , postal_code: str , phone: str ):
    global order_id, discount, coupon_code
    if not config.account_now:
        return Div(P("account Not Found", cls="error-message"))
    acc = OrangeIT.search_acc_by_id(config.account_now)
    order_id = OrangeIT.create_order_acc(config.account_now, full_name, address, city, postal_code ,phone , discount, coupon_code)
    OrangeIT.clear_cart_account_by_id(config.account_now)
    return Style(payment_css), Div(
        Div(A(H1("ORANGE", cls="header-title"), href='/'), cls="header-container"),
        Div(
            H2("💳 Enter Your Credit Card Details",style='color:#000;'),
            Div(
                Form(
                    Label("Card Number:", For="card_number"),
                    Input(id="card_number", type="text", placeholder="1234 5678 9012 3456", required=True),

                    Label("Expiry Date:", For="expiry_date"),
                    Input(id="expiry_date", type="text", placeholder="MM/YY", required=True),

                    Label("CVC:", For="cvc"),
                    Input(id="cvc", type="text", placeholder="123", required=True),

                    Button('Pay Now', type="submit", hx_post='/confirm-payment', cls="pay-button"),
                    cls="card-form"
                ),
                cls="payment-container"
            ),
        ),
        Div(P("© 2025 OrAnGe Store | All Rights Reserved.", cls="footer"), cls="container")
    )

@rt('/confirm-payment/')
def post(card_number:str, expiry_date:str, cvc:str):
    global order_id
    card = OrangeIT.check_card(card_number, expiry_date, cvc)
    if not card:
        return Style(error_css),Div(P("❌ Card invalid", cls="error-message"),cls="error-box")
    
    order_total = OrangeIT.get_order_total(order_id, config.account_now)  # ดึงยอดรวมของคำสั่งซื้อ
    if card.get_amount() < order_total:
        return Style(error_css),Div(P("❌ Insufficient funds. Please use another card.", cls="error-message"),cls="error-box")  # เงินไม่พอ

    # สร้างอ็อบเจ็กต์สำหรับการชำระเงินด้วยบัตรเครดิต
    payment = CreditCardPayment(order_total, card.get_card_number(), "Customer")

    if payment.process_payment():
        OrangeIT.deduct_amount_card(card, order_total)  # หักเงินจากบัตร
        OrangeIT.change_status_order(config.account_now,order_id,'Wait for shipping')
        OrangeIT.clear_cart_account_by_id(config.account_now)  # ล้างตะกร้าสินค้า
        return Redirect('/')

    return Style(error_css),Div(P("❌ Payment failed. Please try again.", cls="error-message"),cls="error-box")  # การชำระเงินล้มเหลว


@rt('/view_myorder')
def get():
    if not config.account_now:
        return Style(error_css),Div(P("Account Not Found", cls="error-message"),cls="error-box")
    
    acc = OrangeIT.search_acc_by_id(config.account_now)
    orders = acc.get_myorder_lst()
    
    return Body(
        Div(
            H1(f'📦 คำสั่งซื้อของฉัน ({len(orders)})', cls='order-header'),
            Table(
                Tr(Th("Order ID"), Th("สินค้า"), Th("สถานะ"), Th("ที่อยู่"), Th("ยอดรวม"), Th("รายละเอียด"), Th("ชำระเงิน")),
                *[
                    Tr(
                        Td(order.get_id()),
                        Td(Ul(*[Li(item.get_product().get_name()) for item in order.get_list()]), cls="order-items"),
                        Td(order.get_status(), cls="order-status"),
                        Td(order.get_address(), cls="order-address"),
                        Td(f"฿{order.get_total_amount()}", cls="order-total"),
                        Td(Button("🔍", cls="view-btn", hx_post=f"/order_details/{order.get_id()}", hx_target="#order-details-container", hx_swap="innerHTML")),
                        
                        # ✅ ส่งฟอร์มไปที่ /re_payment_order แทน /view_myorder
                        Td(
                            Form(
                                Input(type="hidden", name="order", value=order.get_id()),  # ส่งค่า order_id
                                Button("💳 Pay", type="submit", cls="pay-btn"),
                                action='/re_payment_order/',
                                method="post"
                            )
                        ) if order.get_status() == 'Wait For payment' else Td("")
                    ) 
                    for order in orders
                ],
                cls="order-table"
            ),
            Div(id="order-details-container", cls="order-details-container"),
            id="orders"
        ),
        Style(view_order)
    )


@rt('/re_payment_order/')
def post(order:int):
    global order_id
    order_id = order
    return Style(payment_css), Div(
        Div(A(H1("ORANGE", cls="header-title"), href='/'), cls="header-container"),
        Div(
            H2("💳 Enter Your Credit Card Details",style='color:#000;'),
            Div(
                Form(
                    Label("Card Number:", For="card_number"),
                    Input(id="card_number", type="text", placeholder="1234 5678 9012 3456", required=True),

                    Label("Expiry Date:", For="expiry_date"),
                    Input(id="expiry_date", type="text", placeholder="MM/YY", required=True),

                    Label("CVC:", For="cvc"),
                    Input(id="cvc", type="text", placeholder="123", required=True),

                    Button('Pay Now', type="submit", hx_post='/confirm-payment', cls="pay-button"),
                    cls="card-form"
                ),
                cls="payment-container"
            ),
        ),
        Div(P("© 2025 OrAnGe Store | All Rights Reserved.", cls="footer"), cls="container")
    )

@rt('/order_details/{order_id}')
def post(order_id: int):
    if not config.account_now:
        return Style(error_css),Div(P("Account Not Found", cls="error-message"))
    order = OrangeIT.search_order_by_id(config.account_now , order_id)
    if not order:
        return Style(error_css),Div(P("Order not found", cls="error-message"))
    
    return Div(
        H2(f"รายละเอียดคำสั่งซื้อ #{order.get_id()}", cls="order-detail-header"),
        P(f"สถานะ: {order.get_status()}", cls="order-status"),
        P(f"ที่อยู่จัดส่ง: {order.get_address()}", cls="order-address"),
        P(f"ยอดรวม: ฿{order.get_total_amount()}", cls="order-total"),
        P(f"คูปอง : {order.get_coupon()} ลดทั้งหมด : {OrangeIT.search_coupon_by_code(order.get_coupon())}", cls="order-total"),
        H3("รายการสินค้า", cls="order-items-header"),
        Ul(
            *[Li(f"{item.get_product().get_name()} : {item.get_quantity()} ชิ้น (฿{item.get_price_product() * item.get_quantity()})") for item in order.get_list()]
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