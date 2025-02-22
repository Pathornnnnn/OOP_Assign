from fasthtml.common import *
from create_instance import *
OrangeIT = create_instance()
app , rt = fast_app()

# PATH


#/
@rt('/')
def get():
    pass


#/login
@rt('/login')
def get():
    pass



#/register
@rt('/register')
def get():
    pass



#/home
@rt('/')
def get():
    pass



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
