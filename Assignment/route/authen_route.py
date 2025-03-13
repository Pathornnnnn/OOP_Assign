from app import *
from make_app.css import*
import config
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
    acc = OrangeIT.check_login(email, password)
    if acc:
        config.account_now = acc.get_acc_id()
        if not OrangeIT.verify_admin(config.account_now):
            return Redirect("/")  # กลับไปหน้าแรกถ้า Login สำเร็จ
        else:
            return Redirect("/admin_home")
    return "❌ Login Failed! กรุณาตรวจสอบอีเมลหรือรหัสผ่าน", 401  # แจ้งเตือนถ้าข้อมูลผิด

#logout
@rt('/logout')
def get():
    config.account_now = None
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
