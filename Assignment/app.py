from fasthtml.common import *
from make_app.class_orangeit import *
from make_app.create_instance import *
import config  # นำเข้า config.py

global account_now, discount_now, tem_address, coupon_code, UPLOAD_DIR , UPLOAD_DIR2
app, rt = fast_app()
OrangeIT = create_instance()
from route import home_route, product_route, authen_route, member_route, admin_route
serve()