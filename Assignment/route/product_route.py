from app import *
from make_app.css import*
import config
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
                            Button("ซื้อเลย", cls="buy-btn", style='margin-right:5px;margin-bottom:10px', hx_post=f'/purchase/{product.get_id()}')
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
    user = OrangeIT.search_acc_by_id(config.account_now)
    if not user:
        return P("กรุณาเข้าสู่ระบบก่อนรีวิว", cls="error")

    OrangeIT.add_review(config.account_now ,id , rating, review_text)  # บันทึกรีวิวลงระบบ
    return Div(
        P(f"{user.get_name()} ให้คะแนน: {'⭐' * rating}", cls="review-rating"),
        P(review_text, cls="review-text"),
        cls="review"
    )


@rt('/purchase/{product_id}')
def post(product_id : int):
    if not config.account_now:
        return Div(P("account Not Found", cls="error"))
    else:
        OrangeIT.add_to_cart(product_id,1,config.account_now)
        #print result
        temp_acc = OrangeIT.search_acc_by_id(config.account_now)
        print('ID :',temp_acc.get_id(),'| Name :',  temp_acc.get_name() ,'| Cart :', temp_acc.get_cart_shopping())

        return Redirect("/view_cart")

#add_to_cart
@rt('/cart/{product_id}')   
def post(product_id: int , quantity: int=1):
    try:
        quantity = int(quantity)
        if quantity <= 0:
            return Div(P("❌ Invalid quantity!", cls="error"))
    except ValueError:
        return Div(P("❌ Invalid quantity format!", cls="error"))

    if not config.account_now:
        return Div(P("account Not Found", cls="error"))
    else:
        OrangeIT.add_to_cart(product_id,quantity,config.account_now)
        #print result
        temp_acc = OrangeIT.search_acc_by_id(config.account_now)
        print('ID :',temp_acc.get_id(),'| Name :',  temp_acc.get_name() ,'| Cart :', temp_acc.get_cart_shopping())

        return Redirect("/")
