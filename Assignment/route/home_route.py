from app import *
from make_app.css import*
import config
#/home
@rt('/')
def get():
    if config.account_now == None:
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
        ins_acc = OrangeIT.search_acc_by_id(config.account_now)
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
                        ),
                    A(
                                P('Coupons', cls="coupon-btn"),  
                                cls="coupon-link" ,href='/coupons'  
                        ),
                    cls="header-right"   
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
    results = OrangeIT.search_product_by_input(name)
    if results:
        return Div(cls=("product-container"), *[Div(
            Img(src=product.get_img(), alt=product.get_name()),
            H3(product.get_name()),
            P(f"Price : {product.get_price()} THB"),
            cls=("product-card")
        ) for product in results])
    else:
        return Div(P("Products Not Found."))