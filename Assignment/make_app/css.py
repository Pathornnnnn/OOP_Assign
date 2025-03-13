home_css =''' """

                :root {
                    --pico-text-decoration: none;
                }

                a, .login a, .cart a {
                    text-decoration: none !important;
                    border-bottom: none !important;
                    box-shadow: none !important;
                    outline: none !important;
                }

                .login a {
                    text-decoration: none !important;
                    border-bottom: none !important;
                }

                .login p, .cart p {
                    text-decoration: none;
                    font-size: 16px;
                    font-weight: bold;
                    color: black;
                    margin: 0;
                    padding-left: 5px; /* เพิ่มระยะห่างระหว่างไอคอนกับข้อความ */
                    transition: color 0.3s ease-in-out;
                }

                .login:hover p, .cart:hover p {
                    color: #f39c12; /* เปลี่ยนสีเป็นส้มเมื่อ hover */
                }
                html, body {
                    background-color: #ffffff !important; /* บังคับให้เป็นสีขาว */
                    color: black; /* ทำให้ข้อความมองเห็นได้ชัดเจน */
                }
                .container, .product-container {
                    background-color: #ffffff !important;
                }
                body {
                    background-color: #ffffff;
                    margin: 0;
                    padding: 0;
                    min-height: 100vh; /* ใช้ความสูงเต็มหน้าจอ */
                    display: flex;
                    flex-direction: column;
                }

                .header-container {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 15px 20px;
                    background-color: #ffffff; /* Header สีขาว */
                    color: black;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05); /* เงาเบาๆ */
                    position: relative;
                }

                .header-title {
                    font-size: 28px; /* เพิ่มขนาดโลโก้ */
                    font-weight: bold;
                    color: #f39c12;
                }

                .header-buttons {
                    display: flex;
                    gap: 15px;
                    align-items: center;
                }

                .icon {
                    width: 30px;  /* ลดขนาดไอคอน */
                    height: 30px; /* ลดขนาดไอคอน */
                }

                .login {
                    text-decoration: none;
                    display: flex;
                    align-items: center;
                    font-size: 14px;
                    cursor: pointer;
                }

                .login:hover {
                    transform: translateY(-3px);
                }

                .cart:hover {
                    transform: translateY(-3px);
                }
                                        
                .login, .cart {
                    display: flex;
                    align-items: center;
                    gap: 5px;
                    font-size: 16px;
                    cursor: pointer;
                    color: black; /* เปลี่ยนเป็นสีดำ */
                }

                .search-container {
                    display: flex;
                    align-items: center;
                    width: 800px;  /* ลดขนาดกล่องค้นหา */
                    height: 50px;
                    background: white;
                    border-radius: 20px;
                    overflow: hidden;
                    border: 1px solid #ddd;
                }

                .search-input {
                    flex: 1;
                    padding: 10px;
                    font-size: 14px;
                    border: none;
                    outline: none;
                    color: black;
                    background: transparent;
                    text-align: left; /* จัดข้อความไปทางซ้าย */
                }

                .search-input::placeholder {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    text-align: left; /* จัด placeholder ไปทางซ้าย */
                }
                                
                .search-btn {
                    background: transparent;
                    border: none;
                    padding: auto; /* ปรับขนาดปุ่มให้เล็กลง */
                    cursor: pointer;
                }
                                
                .search-input:focus {
                    outline: none;
                    box-shadow: none;
                    border: none;
                }

                .product-container {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                    gap: 20px;
                    padding: 20px;
                    max-width: 1200px;
                    margin: auto;
                }

                .product-card {
                    background-color: #ffffff; /* เปลี่ยนเป็นขาว */
                    padding: 15px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05); /* ลดเงาให้อ่อนลง */
                    text-align: center;
                    transition: transform 0.2s;
                    cursor: pointer;
                }

                .product-card:hover {
                    transform: translateY(-3px);
                }

                .product-card img {
                    width: 100%;
                    height: 200px;
                    object-fit: contain;
                }

                .product-card h3 {
                    font-size: 1em;
                    margin: 10px 0;
                    color: black;
                }

                .product-card p {
                    color: #333; /* เปลี่ยนเป็นสีเทาเข้ม */
                    font-weight: bold;
                    font-size: 1em;
                }
                                
                .container {
                    display: flex;
                    flex-direction: column;
                    min-height: 100vh;
                }
                                
                .footer {
                    background-color: #ffffff !important;
                    color: black;
                    text-align: center;
                    padding: 15px 20px;
                    font-size: 14px;
                    border-top: 1px solid #ddd;
                    margin-top: auto; /* ดัน footer ไปอยู่ล่าง */
                }

                                /* ปรับ container ของปุ่มให้อยู่ชิดขวา */
                .header-right {
                    display: flex;
                    gap: 15px; /* ระยะห่างระหว่าง Cart กับ Coupons */
                    align-items: center;
                }

                /* ปรับปุ่ม Coupons */
                .coupon {
                    display: flex;
                    align-items: center;
                    cursor: pointer;
                    background-color: #FF5500;
                    padding: 5px 10px;
                    border-radius: 6px;
                    transition: 0.3s;
                }

                .coupon:hover {
                    background-color: #E04400;
                }

                .coupon-btn {
                    color: white;
                    font-size: 14px;
                    margin-left: 6px;
                }

                .icon.coupon {
                    width: 20px;
                    height: 20px;
                }
                .coupon-btn {
    font-size: 16px;
    font-weight: bold;
    padding: 10px 16px;
    border: none;
    border-radius: 8px;
    background: linear-gradient(135deg, #FF6600, #FF3300);
    color: white;
    cursor: pointer;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease-in-out;
}

.coupon-btn:hover {
    background: linear-gradient(135deg, #FF5500, #FF2200);
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}

.coupon-btn {
    font-size: 14px;
    font-weight: bold;
    padding: 8px 12px;  /* ลด padding ให้พอดี */
    border: none;
    border-radius: 6px;
    background: linear-gradient(135deg, #FF6600, #FF3300);
    color: white;
    cursor: pointer;
    box-shadow: 0 3px 5px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease-in-out;
    display: inline-flex; /* ทำให้ปุ่มพอดีกับข้อความ */
    align-items: center;
    justify-content: center;
    min-width: auto; /* ป้องกันปุ่มกว้างเกินไป */
}

.coupon-btn:hover {
    background: linear-gradient(135deg, #FF5500, #FF2200);
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}
.coupon-container {
    display: inline-block; /* หรือใช้ inline-flex */
    margin: 0;
    padding: 0;
}
.coupon-link {
    display: inline-block; /* ปรับให้ a มีขนาดพอดีกับเนื้อหา */
    padding: 0; /* ตัด padding ที่อาจทำให้ใหญ่เกิน */
    margin: 0; /* ป้องกัน margin เกิน */
    text-decoration: none; /* เอาขีดเส้นใต้ลิงก์ออก */
}



                

                            """ 
            '''

add_css = '''
            """
                head {
                    background-color:rgb(255, 255, 255);
                }
                body {
                    background-color:rgb(255, 255, 255);
                    margin: 0;
                    padding: 0;
                    min-height: 100vh;
                    display: flex;
                    flex-direction: column;
                    min-height: 100vh;
                }
                .header-container {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 15px 20px;
                    background-color: #ffffff;
                    color: black;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
                    position: relative;
                }
                .header-title {
                    font-size: 28px;
                    font-weight: bold;
                    color: #f39c12;
                }
                .search-container {
                    display: flex;
                    align-items: center;
                    width: 800px;
                    height: 50px;
                    background: white;
                    border-radius: 20px;
                    overflow: hidden;
                    border: 1px solid #ddd;
                }
                .search-input {
                    flex: 1;
                    padding: 10px;
                    font-size: 14px;
                    border: none;
                    outline: none;
                    color: black;
                    background: transparent;
                }
                .search-btn {
                    background: #f39c12;
                    color: white;
                    padding: 10px 15px;
                    border-radius: 0 20px 20px 0;
                    transition: background 0.3s ease;
                }

                a{
                    text-decoration: none;
                    color: inherit;
                }
                .search-btn:hover {
                    background: #e67e22;
                }
                .product-container {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                    gap: 20px;
                    padding: 20px;
                    max-width: 1200px;
                    margin: auto;
                }
                .product-card {
                    background: white;
                    padding: 20px;
                    border-radius: 12px;
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                    transition: all 0.3s ease-in-out;
                }
                .product-card:hover {
                    transform: scale(1.05);
                }
                .footer {
                    background-color: #ffffff;
                    color: black;
                    text-align: center;
                    padding: 15px 20px;
                    font-size: 14px;
                    border-top: 1px solid #ddd;
                    margin-top: auto;
                }
                button {
                    background: #f39c12;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background 0.3s ease-in-out;
                }
                button:hover {
                    background: #e67e22;
                }
                input {
                    background-color: white;
                    color: black;
                    padding: 10px;
                    font-size: 16px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    width: 100%;
                    max-width: 300px;
                    box-sizing: border-box;
                    margin: 5px 0;
                }
                        """

'''


register_css = '''
                """
                    head {
                        background-color:rgb(255, 255, 255);
                    }
                    body {
                        background-color:rgb(255, 255, 255);
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        flex-direction: column;
                    }
                    .register-title {
                        color: rgb(0, 0, 0);
                        text-align: center;
                        font-size: 50px;
                        margin: 20px 0;
                    }
                    .register-container {
                    background: white;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgb(187, 187, 187);
                        width: 300px;
                        text-align: center;
                    }
                    .register-btn {
                        width: 100%;
                        padding: 8px;
                        background-color:rgb(255, 170, 0);
                        color: white;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                    }
                    .register-btn:hover {
                        background-color:rgb(255, 132, 0);
                    }
                    .register-form input, .register-form select {
                        color: rgb(0, 0, 0);
                        background-color:rgb(239, 239, 239);
                        width: 100%;
                        padding: 10px;
                        margin: 10px 0;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                    }
                    """

'''


login_css = '''
                    head {
                        background-color: rgb(255, 255, 255);
                    }
                    a{
                        text-decoration: none;
                        color: inherit;
                    }
                    body {
                        background-color: rgb(255, 255, 255);
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        flex-direction: column;
                    }

                    .login-title {
                        color: #d35400;
                        text-align: center;
                        font-size: 50px;
                        font-weight: bold;
                        margin-bottom: 20px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        gap: 10px;
                    }

                    .signup-container {
                        background: white;
                        padding: 30px;
                        border-radius: 15px;
                        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
                        width: 350px;
                        text-align: center;
                    }

                    .login-form input {
                        color: rgb(0, 0, 0);
                        background-color: rgb(239, 239, 239);
                        width: 100%;
                        padding: 12px;
                        margin: 10px 0;
                        border: 1px solid #ccc;
                        border-radius: 8px;
                        font-size: 16px;
                        transition: all 0.3s ease-in-out;
                    }

                    .login-form input:focus {
                        border-color: #e67e22;
                        outline: none;
                        box-shadow: 0 0 5px rgba(230, 126, 34, 0.5);
                    }

                    .signup-btn {
                        width: 100%;
                        padding: 12px;
                        font-size: 18px;
                        font-weight: bold;
                        background: linear-gradient(135deg, #e67e22, #d35400);
                        color: white;
                        border: none;
                        border-radius: 8px;
                        cursor: pointer;
                        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
                        transition: all 0.3s ease-in-out;
                    }

                    .signup-btn:hover {
                        background: linear-gradient(135deg, #f39c12, #e67e22);
                        transform: translateY(-3px) scale(1.05);
                        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.25);
                    }

                    .signup-btn:active {
                        transform: scale(0.95);
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    }

        '''


product_css = '''

html, body {
    background-color: #ffffff !important;
    color: black;
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
}
a{
                        text-decoration: none;
                        color: inherit;
                    }

.container, .product-container {
    background-color: #ffffff !important;
}

body {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

/* Header */
.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 20px;
    background-color: #ffffff;
    color: black;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}

.header-title {
    font-size: 32px;
    font-weight: bold;
    color: #f39c12;
}

/* Product Detail */
.product-detail-container {
    display: flex;
    gap: 30px;
    max-width: 900px;
    margin: auto;
    padding: 30px;
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Product Image */
.product-image-container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 400px;
}

.product-image {
    width: 300px !important;
    height: auto !important;
    object-fit: contain;
    display: block;
    border-radius: 10px;
}

/* Product Info */
.product-info {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.product-info h2 {
    font-size: 24px;
    font-weight: bold;
    color: #333;
}

.product-info p {
    font-size: 16px;
    color: #555;
}

/* Quantity Input */
input[type="number"] {
    width: 80px;
    padding: 8px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Buttons */
.buy-btn {
    background-color: #f39c12;
    color: white;
    padding: 12px 18px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 18px;
    transition: 0.3s;
}

.buy-btn:hover {
    background-color: #e67e22;
}

.add-cart-btn {
    background-color: gray;
    color: white;
    padding: 12px 18px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 18px;
    transition: 0.3s;
}

.add-cart-btn:hover {
    background-color: #555;
}

/* Review Section */
.review-container {
    max-width: 900px;
    margin: auto;
    margin-top: 20px;
    padding: 20px;
    background: #fafafa;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.review-title {
    font-size: 22px;
    font-weight: bold;
    color: #333;
    margin-bottom: 10px;
}

.review {
    background: white;
    padding: 12px;
    margin-bottom: 8px;
    border-left: 5px solid #f4a261;
    font-size: 14px;
    border-radius: 5px;
}

.review-rating {
    font-weight: bold;
    color: #f4a261;
}

.review-text {
    font-size: 14px;
    color: #444;
}

/* Review Button */
.review-btn {
    margin-top: 15px;
    background-color: #f4a261;
    color: white;
    border: none;
    padding: 12px 16px;
    cursor: pointer;
    font-size: 16px;
    border-radius: 6px;
    transition: 0.3s;
}

.review-btn:hover {
    background-color: #e76f51;
}

/* Footer */
.footer {
    background-color: #ffffff !important;
    color: black;
    text-align: center;
    padding: 15px 20px;
    font-size: 14px;
    border-top: 1px solid #ddd;
    margin-top: auto;
}

'''

checkout_css = '''

                :root {
                    --pico-text-decoration: none;
                }

                a, .login a, .cart a {
                    text-decoration: none !important;
                    border-bottom: none !important;
                    box-shadow: none !important;
                    outline: none !important;
                }
                   /* ✅ Checkout Container */
.checkout-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    margin-top: 20px;
}

/* ✅ Checkout Form */
.checkout-form {
    background: #fff;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    width: 90%;
    max-width: 400px;
    display: flex;
    flex-direction: column;
    gap: 15px;
}

/* ✅ Form Title */
.form-title {
    font-size: 22px;
    font-weight: bold;
    text-align: center;
    color: #333;
}

/* ✅ Input Fields */
.checkout-form input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 16px;
    transition: 0.3s;
}

.checkout-form input:focus {
    border-color: #ff6a00;
    box-shadow: 0 0 5px rgba(255, 106, 0, 0.3);
    outline: none;
}

/* ✅ Total Price */
.total-price {
    font-size: 18px;
    font-weight: bold;
    text-align: center;
    color: #ff6a00;
}

/* ✅ Buttons */
.checkout-btn, .coupon-btn {
    width: 100%;
    padding: 12px;
    background: #ff6a00;
    color: #fff;
    border: none;
    border-radius: 8px;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
}

.checkout-btn:hover, .coupon-btn:hover {
    background: #e55b00;
}
/* ✅ ตั้งค่าพื้นหลังขาวสะอาด */
body {
    background-color: #fff;
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
}

/* ✅ โลโก้ OrangeIT */
.header-title {
    font-size: 28px;
    font-weight: bold;
    text-align: center;
    color: #ff6a00; /* สีส้มเด่น */
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-top: 20px;
}

/* ✅ Checkout Title */
.checkout-title {
    font-size: 26px;
    font-weight: bold;
    text-align: center;
    color: #333; /* สีดำเทา */
    margin-top: 15px;
}
/* ✅ ปุ่ม Coupon เป็นสีน้ำเงิน */
.coupon-btn {
    background-color: #007bff; /* 🔵 สีน้ำเงินสด */
    color: white;
    font-size: 16px;
    font-weight: bold;
    padding: 10px 20px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.3s ease-in-out;
}

/* ✅ Hover Effect: เปลี่ยนเป็นน้ำเงินเข้ม */
.coupon-btn:hover {
    background-color: #0056b3;
}
/* ✅ ปรับพื้นหลังช่องรับค่าเป็นสีขาว */
.input-field {
    background-color: white;  /* ⚪ พื้นหลังสีขาว */
    color: #333;              /* 🔘 สีตัวอักษรเข้มขึ้น */
    font-size: 16px;
    padding: 10px;
    border: 1px solid #ccc;  /* 🔲 เส้นขอบสีเทา */
    border-radius: 5px;
    width: 100%;
    box-sizing: border-box; /* ✅ ป้องกันขยายเกินขอบ */
}

/* ✅ เมื่อกดที่ช่องให้มีขอบสีฟ้า */
.input-field:focus {
    border-color: #007bff;  /* 🔵 เปลี่ยนเป็นขอบน้ำเงิน */
    outline: none;
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.5); /* ✨ เพิ่มเงาฟ้า */
}

'''

# payment_css = '''
#                 """
#                 :root {
#                     --pico-text-decoration: none;
#                 }
#                     body {
#                         background-color: #ffffff;
#                         color: black;
#                         margin: 0;
#                         padding: 0;
#                         min-height: 100vh;
#                         display: flex;
#                         flex-direction: column;
#                         align-items: center;
#                     }
                    
#                     .container {
#                         width: 100%;
#                         max-width: 800px;
#                         background: white;
#                         padding: 20px;
#                         border-radius: 10px;
#                         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#                         text-align: center;
#                         margin-top: 50px;
#                     }

#                     .payment-title {
#                         font-size: 24px;
#                         font-weight: bold;
#                         color: #f39c12;
#                         margin-bottom: 20px;
#                     }

#                     .payment-form {
#                         display: flex;
#                         flex-direction: column;
#                         gap: 15px;
#                     }

#                     .payment-form label {
#                         font-size: 16px;
#                         font-weight: bold;
#                         text-align: left;
#                         color: #555;
#                     }

#                     .payment-form input, .payment-form select {
#                         width: 100%;
#                         padding: 10px;
#                         font-size: 16px;
#                         border: 1px solid #ccc;
#                         border-radius: 5px;
#                         box-sizing: border-box;
#                         background-color: #f8f9fa;
#                         color: #333;
#                     }

#                     .payment-form input::placeholder {
#                         color: #888;
#                     }

#                     .payment-btn {
#                         background-color: #f39c12;
#                         color: white;
#                         padding: 12px;
#                         border: none;
#                         border-radius: 5px;
#                         cursor: pointer;
#                         font-size: 18px;
#                         transition: background 0.3s ease-in-out;
#                     }

#                     .payment-btn:hover {
#                         background-color: #e67e22;
#                     }

#                     .footer {
#                         background-color: #ffffff;
#                         color: black;
#                         text-align: center;
#                         padding: 15px 20px;
#                         font-size: 14px;
#                         border-top: 1px solid #ddd;
#                         margin-top: auto;
#                     }

#                     .checkout-container label {
#                         font-weight: bold;
#                         display: block;
#                         margin-top: 10px;
#                         color: #000; /* เปลี่ยนเป็นสีดำ */
#                     }
    
#                     h3, h2, p {
#                         color: #000; /* เปลี่ยนเป็นสีดำ */
#                     }

#                     .footer {
#                         text-align: center;
#                         margin-top: 20px;
#                         color: #000; /* เปลี่ยนเป็นสีดำ */
#                         font-size: 14px;
#                     }

#                     """
# '''

payment_css = '''
:root {
                    --pico-text-decoration: none;
                }

                a {
                    text-decoration: none !important;
                    border-bottom: none !important;
                    box-shadow: none !important;
                    outline: none !important;
                }
                body{
                background-color:#fff;}

/* ทำให้ Container อยู่ตรงกลางและดูสะอาด */
.payment-container {
    max-width: 400px;
    margin: 50px auto;
    padding: 20px;
    background: #ffffff;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
    text-align: center;
    color: #000;
}

/* หัวข้อหลักของหน้า */
.header-title {
    font-size: 30px;
    font-weight: bold;
    color: #FF6600;
    text-align: center;
}

/* แบบฟอร์มบัตรเครดิต */
.card-form {
    display: flex;
    flex-direction: column;
    gap: 15px;
    text-align: left;
    padding: 10px;
}

.card-form label {
    font-weight: 600;
    color: #333;
    font-size: 14px;
}

.card-form input {
    width: 100%;
    padding: 12px;
    font-size: 16px;
    border: 2px solid #ddd;
    border-radius: 8px;
    transition: all 0.3s ease-in-out;
}

.card-form input:focus {
    border-color: #FF6600;
    outline: none;
    box-shadow: 0px 0px 5px rgba(255, 102, 0, 0.5);
}

/* ปุ่มชำระเงิน */
.pay-button {
    background: #FF6600;
    color: white;
    font-size: 18px;
    padding: 12px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.3s ease-in-out;
}

.pay-button:hover {
    background: #E65C00;
}

/* Footer */
.footer {
    margin-top: 20px;
    font-size: 14px;
    color: #777;
    text-align: center;
}

/* ปรับสีตัวอักษรให้เข้มขึ้น */
.header-title {
    font-size: 30px;
    font-weight: bold;
    color: #FF6600;
    text-align: center;
}

/* ทำให้ข้อความหัวข้อดูเข้มขึ้นและไม่มีเส้นใต้ */
h2 {
    font-size: 22px;
    font-weight: 700;
    color: #000;
    text-align: center;
    text-decoration: none; /* เอาเส้นใต้ออก */
}

/* ปรับสไตล์ของ Input ให้ดูเรียบขึ้น */
.card-form input {
    background-color: #fff; /* เปลี่ยนพื้นหลังเป็นสีขาว */
    color: #333; /* เปลี่ยนฟอนต์ให้เป็นสีเข้ม */
    border: 2px solid #ddd; /* กำหนดขอบให้ดูสะอาด */
    padding: 12px;
    font-size: 16px;
    border-radius: 8px;
    transition: all 0.3s ease-in-out;
}

.card-form input:focus {
    border-color: #FF6600;
    outline: none;
    box-shadow: 0px 0px 5px rgba(255, 102, 0, 0.5);
}

/* ปรับให้ปุ่มดูเด่นขึ้น */
.pay-button {
    background: #FF6600;
    color: white;
    font-size: 18px;
    font-weight: bold; /* ทำให้ตัวอักษรหนาขึ้น */
    padding: 12px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.3s ease-in-out;
}

.pay-button:hover {
    background: #E65C00;
}


'''
view_cart_css = '''
                    .cart-header {
                        text-align: center;
                        font-size: 28px;
                        font-weight: bold;
                        color: #ffcc00;
                        margin-bottom: 20px;
                        text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.2);
                    }

                    .cart-table {
                        width: 100%;
                        border-collapse: collapse;
                        background: #1e1e1e;
                        border-radius: 10px;
                        overflow: hidden;
                        box-shadow: 0 4px 8px rgba(255, 255, 255, 0.1);
                    }

                    .cart-table th {
                        background: #f4a261;
                        color: white;
                        padding: 12px;
                        text-align: center;
                        font-size: 1.2rem;
                    }

                    .cart-table td {
                        padding: 12px;
                        text-align: center;
                        border-bottom: 1px solid #444;
                        color: #fff;
                    }

                    .cart-table tr:hover {
                        background: rgba(255, 255, 255, 0.1);
                    }

                    .qty-form {
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    }

                    .qty-btn {
                        background: #f4a261;
                        color: white;
                        border: none;
                        padding: 8px 12px;
                        cursor: pointer;
                        font-size: 16px;
                        border-radius: 5px;
                        transition: background 0.3s ease-in-out;
                    }

                    .qty-btn:hover {
                        background: #e76f51;
                    }

                    .qty-span {
                        font-size: 18px;
                        font-weight: bold;
                        margin: 0 10px;
                    }

                    .total-price {
                        font-size: 22px;
                        font-weight: bold;
                        color: #28a745;
                        text-align: right;
                        margin-top: 20px;
                    }

                    .checkout-btn {
                        display: block;
                        width: 100%;
                        padding: 12px;
                        background: #2a9d8f;
                        color: white;
                        text-align: center;
                        font-size: 20px;
                        font-weight: bold;
                        border: none;
                        border-radius: 6px;
                        cursor: pointer;
                        margin-top: 20px;
                        transition: background 0.3s ease-in-out;
                    }

                    .checkout-btn:hover {
                        background: #21867a;
                    }
'''


popup_css = '''
                """
                    .popup {
                        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                        background: rgba(0, 0, 0, 0.5); display: flex;
                        align-items: center; justify-content: center; z-index: 1000;
                    }
                    .popup-content {
                        background: white; padding: 20px; border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.25);
                        min-width: 300px; text-align: center;
                    }
                    .popup button {
                        margin-top: 10px; padding: 5px 10px; border: none; background: #ff5b5b;
                        color: white; border-radius: 5px; cursor: pointer;
                    }
                    .popup button:hover {
                        background: #ff2b2b;
                    }
                """

'''
view_order = """
            head {
                background-color: rgb(255, 255, 255);
            }

            body {
                font-family: 'Arial', sans-serif;
                background-color: #121212; /* สีพื้นหลังเข้ม */
                color: #fff;
            }

            .order-header {
                font-size: 1.5rem;
                font-weight: bold;
                margin-bottom: 1rem;
            }

            .order-table {
                width: 100%;
                border-collapse: collapse;
                background: #1e1e1e;
                border-radius: 10px;
                overflow: hidden;
                box-shadow: 0 4px 8px rgba(255, 255, 255, 0.1);
            }

            .order-table th {
                background: #333;
                color: #ffcc00;
                padding: 12px;
                text-align: left;
                font-size: 1rem;
            }

            .order-table td {
                padding: 12px;
                border-bottom: 1px solid #444;
            }

            .order-table tr:hover {
                background: rgba(255, 255, 255, 0.1);
            }

            .order-status {
                font-weight: bold;
                color: #ffcc00;
                background: rgba(255, 204, 0, 0.2);
                padding: 8px;
                border-radius: 5px;
                text-align: center;
            }

            .order-total {
                font-weight: bold;
                color: #28a745;
            }

            .order-address {
                color: #bbb;
            }

            .view-btn {
                background: #007bff;
                color: white;
                padding: 8px 12px;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                transition: background 0.3s ease-in-out;
            }

            .view-btn:hover {
                background: #0056b3;
            }
        """

admin_home_css = '''
                    .admin-header {
                        text-align: center;
                        font-size: 32px;
                        font-weight: bold;
                        margin-bottom: 20px;
                        color: #d35400;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        gap: 10px;
                    }

                    .admin-menu {
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        gap: 20px;
                        margin-top: 30px;
                    }

                    .admin-btn {
                        background: linear-gradient(135deg, #e67e22, #d35400);
                        color: white;
                        padding: 14px 28px;
                        font-size: 20px;
                        font-weight: bold;
                        border: none;
                        border-radius: 12px;
                        cursor: pointer;
                        text-decoration: none;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        gap: 10px;
                        width: 260px;
                        text-align: center;
                        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
                        transition: all 0.3s ease-in-out;
                    }

                    a{
                        text-decoration: none;
                        color: inherit;
                    }

                    .admin-btn a {
                        text-decoration: none;
                        color: inherit;
                    }

                    .admin-btn:hover {
                        transform: translateY(-3px) scale(1.05);
                        background: linear-gradient(135deg, #f39c12, #e67e22);
                        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.25);
                    }

                    .admin-btn:active {
                        transform: scale(0.95);
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    }


''' 



verify_order = '''
                    """
                    .verify-header {
                        text-align: center;
                        font-size: 32px;
                        font-weight: bold;
                        margin-bottom: 20px;
                        color: #28a745;
                        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
                    }

                    .order-table {
                        width: 100%;
                        border-collapse: collapse;
                        margin-top: 20px;
                        background: white;
                        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
                        border-radius: 10px;
                        overflow: hidden;
                    }

                    .order-table th, .order-table td {
                        border: 1px solid #ddd;
                        padding: 12px;
                        text-align: center;
                        font-size: 16px;
                    }

                    .order-table th {
                        background: linear-gradient(135deg, #28a745, #218838);
                        color: white;
                        font-size: 18px;
                        font-weight: bold;
                    }

                    .order-items {
                        text-align: left;
                    }

                    .approve-btn, .reject-btn {
                        padding: 8px 14px;
                        font-size: 16px;
                        font-weight: bold;
                        border: none;
                        border-radius: 6px;
                        cursor: pointer;
                        transition: all 0.3s ease-in-out;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
                    }

                    .approve-btn {
                        background: linear-gradient(135deg, #28a745, #218838);
                        color: white;
                    }

                    .approve-btn:hover {
                        background: linear-gradient(135deg, #34d058, #28a745);
                        transform: translateY(-2px) scale(1.05);
                        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
                    }

                    .reject-btn {
                        background: linear-gradient(135deg, #dc3545, #c82333);
                        color: white;
                    }

                    .reject-btn:hover {
                        background: linear-gradient(135deg, #e74c3c, #dc3545);
                        transform: translateY(-2px) scale(1.05);
                        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
                    }
                """

'''

manage_product_css = '''
                        .manage-header {
                            text-align: center;
                            font-size: 24px;
                            font-weight: bold;
                            margin-bottom: 20px;
                        }

                        .add-btn {
                            display: block;
                            margin: 10px auto;
                            padding: 10px;
                            background-color: #2a9d8f;
                            color: white;
                            text-align: center;
                            font-size: 18px;
                            border: none;
                            cursor: pointer;
                        }

                        .add-btn:hover {
                            background-color: #21867a;
                        }

                        .product-table {
                            width: 100%;
                            border-collapse: collapse;
                            margin-top: 20px;
                        }

                        .product-table th, .product-table td {
                            border: 1px solid #ddd;
                            padding: 10px;
                            text-align: center;
                        }

                        .product-table th {
                            background-color: #f4a261;
                            color: white;
                        }

                        .edit-btn, .delete-btn {
                            background-color: #f4a261;
                            color: white;
                            border: none;
                            padding: 5px 10px;
                            cursor: pointer;
                            font-size: 14px;
                            margin: 0 5px;
                        }

                        .edit-btn:hover {
                            background-color: #e76f51;
                        }

                        .delete-btn {
                            background-color: #ff5b5b;
                        }

                        .delete-btn:hover {
                            background-color: #ff2b2b;
                        }



'''


edit_product_css = '''
                    .edit-header {
                        text-align: center;
                        font-size: 28px;
                        font-weight: bold;
                        margin-bottom: 20px;
                        color: #333;
                    }

                    .edit-form {
                        max-width: 400px;
                        margin: 0 auto;
                        padding: 20px;
                        background: #fff;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        display: flex;
                        flex-direction: column;
                    }

                    .edit-form label {
                        font-size: 16px;
                        font-weight: bold;
                        margin-bottom: 5px;
                        color: #555;
                    }

                    .edit-form input {
                        width: 100%;
                        padding: 10px;
                        margin-bottom: 15px;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                        font-size: 16px;
                    }

                    .edit-form input:focus {
                        border-color: #007bff;
                        outline: none;
                    }

                    .save-btn {
                        width: 100%;
                        padding: 12px;
                        background-color: #28a745;
                        color: white;
                        font-size: 18px;
                        font-weight: bold;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        transition: background 0.3s ease;
                    }

                    .save-btn:hover {
                        background-color: #218838;
                    }



'''

coupon_css = '''/* ปรับพื้นหลังให้อ่อนขึ้น */
:root {
                    --pico-text-decoration: none;
                }

                a {
                    text-decoration: none !important;
                    border-bottom: none !important;
                    box-shadow: none !important;
                    outline: none !important;
                }
/* พื้นหลังสีเข้มขึ้น */
body {
    background-color: #eeeeee;
    font-family: Arial, sans-serif;
}

/* หัวข้อหลัก */
.header-title {
    font-size: 28px;
    font-weight: bold;
    color: #FF5500;
    text-align: center;
    margin-bottom: 20px;
}

/* กล่องคูปอง */
.coupon-section {
    text-align: center;
    max-width: 600px;
    margin: 0 auto;
    background: #1a1a1a;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
}

/* ตารางคูปอง */
.coupon-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
    border-radius: 10px;
    overflow: hidden;
    background: #222;
    color: #fff;
}

/* หัวตาราง */
.coupon-table th {
    background-color: #FF5500;
    color: white;
    padding: 14px;
    font-size: 16px;
}

/* แถวข้อมูล */
.coupon-table td {
    padding: 12px;
    border-bottom: 1px solid #444;
}

/* สลับสีแถว */
.coupon-table tr:nth-child(even) {
    background-color: #333;
}

/* Footer */
.footer {
    text-align: center;
    font-size: 14px;
    color: #000;
    margin-top: 20px;
}



'''

error_css = '''
.error-box {
        background-color: #ffe6e6;  /* สีแดงอ่อน */
        border: 1px solid #ff4d4d;  /* เส้นขอบแดง */
        border-radius: 10px;  /* ขอบมน */
        padding: 15px;  /* ระยะห่างข้างใน */
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); /* เงา */
        width: fit-content;
        margin: 10px auto; /* จัดกึ่งกลาง */
    }

    .error-message {
        color: #cc0000;  /* สีแดงเข้ม */
        font-size: 16px;
        font-weight: bold;
    }


'''