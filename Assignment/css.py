home_css =''' """
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
                    .login-title {
                        color: rgb(0, 0, 0);
                        text-align: center;
                        font-size: 50px;
                        margin: 20px 0;
                    }
                    .signup-container {
                        background: white;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgb(187, 187, 187);
                        width: 300px;
                        text-align: center;
                    }
                    .signup-btn {
                        width: 100%;
                        padding: 8px;
                        background-color:rgb(255, 170, 0);
                        color: white;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                    }
                    .signup-btn:hover {
                        background-color:rgb(255, 132, 0);
                    }
                    .login-form input {
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


