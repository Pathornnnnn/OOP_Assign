home_css =''' """
                .login p, .cart p {
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
                    """
                        html, body {
                            background-color: #ffffff !important;
                            color: black;
                        }
                        .container, .product-container {
                            background-color: #ffffff !important;
                        }
                        body {
                            margin: 0;
                            padding: 0;
                            min-height: 100vh;
                            display: flex;
                            flex-direction: column;
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
                        .product-detail-container {
                            display: flex;
                            gap: 20px;
                            max-width: 1000px;
                            margin: auto;
                            padding: 20px;
                            background: #fff;
                            border-radius: 10px;
                            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                        }
                        .product-image-container {
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            width: 360px;
                            height: 360px;
                        }
                        .product-image img {
                            width: 150px !important;
                            height: 150px !important;
                            object-fit: cover;
                            display: block;
                            border-radius: 10px;
                        }
                        .product-info {
                            flex: 1;
                            display: flex;
                            flex-direction: column;
                            gap: 10px;
                        }
                        .buy-btn {
                            background-color: #f39c12;
                            color: white;
                            padding: 10px;
                            border: none;
                            border-radius: 5px;
                            cursor: pointer;
                            font-size: 18px;
                        }
                        .footer {
                            background-color: #ffffff !important;
                            color: black;
                            text-align: center;
                            padding: 15px 20px;
                            font-size: 14px;
                            border-top: 1px solid #ddd;
                            margin-top: auto;
                        }
        """

'''

checkout_css = '''
                    """
                    .coupon-btn {
                        background: #f39c12;
                        color: white;
                        padding: 8px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        margin-left: 10px;
                        font-size: 14px;
                        transition: 0.3s ease-in-out;
                    }

                    .coupon-btn:hover {
                        background: #e67e22;
                    }

                    .error {
                        color: red;
                        font-weight: bold;
                    }

                    .total-price {
                        font-size: 20px;
                        font-weight: bold;
                        color: #e67e22;
                    }


                    head {
                        background-color: #ffffff;
                    }
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #ffffff;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                    }
                    .container {
                        width: 50%;
                        padding: 20px;
                        background: white;
                        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                        margin-top: 50px;
                        border-radius: 10px;
                    }
                    h2 {
                        color: #f39c12;
                        text-align: center;
                    }
                    .order-summary {
                        padding: 10px;
                        border-bottom: 1px solid #ddd;
                    }
                    .total {
                        font-weight: bold;
                        font-size: 18px;
                    }
                    .checkout-btn {
                        background: #f39c12;
                        color: white;
                        padding: 10px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        display: block;
                        width: 100%;
                        text-align: center;
                        margin-top: 20px;
                        font-size: 16px;
                    }
                    .checkout-btn:hover {
                        background: #e67e22;
                    }
                    
                    /* ปรับแต่งฟอร์มที่อยู่ */
                    .checkout-container label {
                        font-weight: bold;
                        display: block;
                        margin-top: 10px;
                        color: #555;
                    }

                    .input-field {
                        width: 100%;
                        padding: 10px;
                        margin: 5px 0;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                        font-size: 16px;
                        background-color: #f8f9fa;
                        color: #333;
                    }

                    .input-field::placeholder {
                        color: #888;
                    }
                    """
'''

payment_css = '''
                """
                    body {
                        background-color: #ffffff;
                        color: black;
                        margin: 0;
                        padding: 0;
                        min-height: 100vh;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                    }
                    
                    .container {
                        width: 100%;
                        max-width: 800px;
                        background: white;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                        text-align: center;
                        margin-top: 50px;
                    }

                    .payment-title {
                        font-size: 24px;
                        font-weight: bold;
                        color: #f39c12;
                        margin-bottom: 20px;
                    }

                    .payment-form {
                        display: flex;
                        flex-direction: column;
                        gap: 15px;
                    }

                    .payment-form label {
                        font-size: 16px;
                        font-weight: bold;
                        text-align: left;
                        color: #555;
                    }

                    .payment-form input, .payment-form select {
                        width: 100%;
                        padding: 10px;
                        font-size: 16px;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                        box-sizing: border-box;
                        background-color: #f8f9fa;
                        color: #333;
                    }

                    .payment-form input::placeholder {
                        color: #888;
                    }

                    .payment-btn {
                        background-color: #f39c12;
                        color: white;
                        padding: 12px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        font-size: 18px;
                        transition: background 0.3s ease-in-out;
                    }

                    .payment-btn:hover {
                        background-color: #e67e22;
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
                    """
'''

payment_css = '''
body {
    background-color: #f8f9fa;
    color: #333;
    margin: 0;
    padding: 0;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-family: Arial, sans-serif;
}

.container {
    width: 100%;
    max-width: 600px;
    background: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    margin-top: 20px;
}

.header-title {
    font-size: 28px;
    font-weight: bold;
    color: #ff7f50;
    text-decoration: none;
}

.payment-container {
    padding: 20px;
}

.qr-container {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.qr-code {
    border-radius: 10px;
    padding: 10px;
    background: white;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.footer {
    margin-top: 20px;
    font-size: 14px;
    color: #888;
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