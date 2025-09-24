import mysql.connector as db

# Database connection
con = db.connect(
    user='root',
    password='JhansiRani@1266',  # your MySQL password
    host='localhost',
    database='project'
)
cur = con.cursor()

# -------------------- ADMIN FUNCTIONS --------------------
def admin_login():
    admin_id = "abc"
    admin_password = "abc"
    while True:
        admin_ID = input("Enter admin id: ")
        admin_PASSWORD = input("Enter admin password: ")
        if admin_id == admin_ID and admin_password == admin_PASSWORD:
            print("Admin logged in successfully!")
            admin_menu()
            return
        else:
            print("Invalid Admin ID or Password")

def admin_view_menu():
    cur.execute('select * from menu')
    values = cur.fetchall()
    print("\n--Menu Items--")
    for i in values:
        print(i[0], '-', i[1], '-', i[2], '-', '₹', i[3])

def add_menu():
    while True:
        choose_add_menu = input("Do you want to add items to menu(yes/no): ")
        if choose_add_menu.lower() == 'yes':
            item_id = int(input("Enter item id: "))
            item_name = input("Enter item name: ")
            item_category = input("Enter item category: ")
            price = int(input("Enter item price: "))
            query = "insert into menu (item_id, item_name, item_category, price) values (%s, %s, %s, %s)"
            values = (item_id, item_name, item_category, price)
            cur.execute(query, values)
            con.commit()
            print("Item added successfully!")
        elif choose_add_menu.lower() == 'no':
            return
        else:
            print("Please enter valid option(yes/no)")

def delete_menu():
    while True:
        choose_delete_menu = input("Do you want to delete items from menu(yes/no): ")
        if choose_delete_menu.lower() == 'yes':
            item_id = int(input("Enter item id to delete: "))
            query = "delete from menu where item_id=%s"
            cur.execute(query, (item_id,))
            con.commit()
            print("Item deleted successfully!")
        elif choose_delete_menu.lower() == 'no':
            return
        else:
            print("Please enter valid option(yes/no)")

def modify_menu():
    while True:
        choose_modify_menu = input("Do you want to modify items in menu(yes/no): ")
        if choose_modify_menu.lower() == 'yes':
            item_id = int(input("Enter the item id you want to modify: "))
            cur.execute("select * from menu where item_id=%s", (item_id,))
            item = cur.fetchone()
            if not item:
                print("Item not found!")
                return
            print(f"Current: ID={item[0]}, Name={item[1]}, Category={item[2]}, Price={item[3]}")
            new_name = input("Enter new name (leave blank to keep same): ") or item[1]
            new_cat = input("Enter new category (leave blank to keep same): ") or item[2]
            new_price = input("Enter new price (leave blank to keep same): ")
            new_price = int(new_price) if new_price.strip() != "" else item[3]
            query = "update menu set item_name=%s, item_category=%s, price=%s where item_id=%s"
            cur.execute(query, (new_name, new_cat, new_price, item_id))
            con.commit()
            print("Item updated successfully!")
        elif choose_modify_menu.lower() == 'no':
            return
        else:
            print("Please enter valid option(yes/no)")

def view_all_order_details():
    while True:
        choose_view_all_order_details = input("Do you want to view all order details(yes/no): ")
        if choose_view_all_order_details.lower() == 'yes':
            query = """
                select o.order_id, u.user_name, m.item_name, oi.qty, m.price, (oi.qty * m.price) as total_price
                from orders o
                join user_details u on o.user_id = u.user_id
                join order_items oi on o.order_id = oi.order_id
                join menu m on oi.item_id = m.item_id
            """
            cur.execute(query)
            rows = cur.fetchall()
            print("\n--- All Order Details ---")
            for row in rows:
                print("Order ID:", row[0], "| User:", row[1], "| Item:", row[2], "| Qty:", row[3], "| Price:", row[4], "| Total:", row[5])    
        elif choose_view_all_order_details.lower() == 'no':
            return
        else:
            print("Please enter valid option (yes/no)")

def show_day_wise_profit():
    while True:
        choose_show_day_wise_profit = input("Do you want to view day wise profit (yes/no): ")
        if choose_show_day_wise_profit.lower() == 'yes':
            order_date = input("Enter valid date (yyyy-mm-dd): ")
            query = """
                select o.order_date, sum(oi.qty * m.price) as day_profit
                from orders o
                join order_items oi on o.order_id = oi.order_id
                join menu m on oi.item_id = m.item_id
                where o.order_date = %s
                group by o.order_date
            """
            cur.execute(query, (order_date,))
            result = cur.fetchone()
            if result:
                print(f"\nDate: {result[0]} | Profit: {result[1]}")
            else:
                print("No orders found on this date.")
        elif choose_show_day_wise_profit.lower() == 'no':
            return
        else:
            print("Please enter valid option (yes/no)")

def admin_menu():
    while True:
        print("\n" + "*"*30)
        print("Admin Menu")
        print("*"*30)
        print("1. View Menu")
        print("2. Add Menu")
        print("3. Delete Menu")
        print("4. Modify Menu")
        print("5. View all order details")
        print("6. Show day wise profit")
        print("7. Logout")
        choose = input("Choose option(1/2/3..): ")
        if choose == "1":
            admin_view_menu()
        elif choose == "2":
            add_menu()
        elif choose == "3":
            delete_menu()
        elif choose == "4":
            modify_menu()
        elif choose == "5":
            view_all_order_details()
        elif choose == "6":
            show_day_wise_profit()
        elif choose == "7":
            print("Admin logout successful")
            return
        else:
            print("Please choose valid option(1/2/3...)")

# -------------------- USER FUNCTIONS --------------------
def user_login():
    user_name = input("Enter your name: ")
    while True:
        user_mobile_number = input("Enter your mobile number: ")
        if user_mobile_number.isdigit() and len(user_mobile_number) == 10 and user_mobile_number[0] in ['9','8','7','6']: 
            print("Valid Mobile Number")
            query = "insert into user_details (user_name, mobile_number) values (%s, %s)"
            cur.execute(query, (user_name, user_mobile_number))
            con.commit()
            print("User registered successfully!")
            user_menu()
            return   
        else:
            print("Invalid Mobile Number")

def user_view_menu():
    cur.execute('select * from menu')
    values = cur.fetchall()
    print("\n--- MENU ITEMS ---")
    for i in values:
        print(i[0], '-', i[1], '-', i[2], '-', '₹', i[3])

def view_all_user_details():
    cur.execute('select * from user_details')
    values = cur.fetchall()
    print("\n--- USERS ---")
    for i in values:
        print(i[0], '-', i[1], '-', i[2])

def add_item_to_cart():
    cart_id = int(input("Enter cart id(1/2/3..): "))
    user_id = int(input("Enter user id(1/2/3..): "))
    item_id = int(input("Enter Item id(1/2/3..): "))
    qty = int(input("Enter quantity: "))

    query = "INSERT INTO cart (cart_id, user_id, item_id, quantity) VALUES (%s, %s, %s, %s)"
    cur.execute(query, (cart_id, user_id, item_id, qty))
    con.commit()
    print("Item added to cart successfully!")

def modify_cart():
    cart_id = int(input("Enter cart id: "))
    new_qty = int(input("Enter new quantity: "))
    query = "UPDATE cart SET quantity=%s WHERE cart_id=%s"
    cur.execute(query, (new_qty, cart_id))
    con.commit()
    print("Cart updated successfully!")

def delete_item():
    cart_id = int(input("Enter cart id to delete: "))
    query = "DELETE FROM cart WHERE cart_id=%s"
    cur.execute(query, (cart_id,))
    con.commit()
    print("Item deleted from cart successfully!")

def user_menu():
    while True:
        print("\n" + "*"*30)
        print("User Menu")
        print("*"*30)
        print("1. View Menu")
        print("2. View All Users")
        print("3. Add Item to Cart")
        print("4. Modify Cart")
        print("5. Delete Item from Cart")
        print("6. Logout")

        choose = input("Choose option: ")
        if choose == "1":
            user_view_menu()
        elif choose == "2":
            view_all_user_details()
        elif choose == "3":
            add_item_to_cart()
        elif choose == "4":
            modify_cart()
        elif choose == "5":
            delete_item()
        elif choose == "6":
            print("User logout successful")
            return
        else:
            print("Please choose valid option")

# -------------------- MAIN MENU --------------------
def Menu():
    while True:
        print("\n" + "*"*30)
        print("Login Page")
        print("*"*30)
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")
        choose = input("Choose login option: ")
        if choose == "1":
            admin_login()
        elif choose == "2":
            user_login()
        elif choose == "3":
            print("Thank you for visiting our restaurant!")
            return
        else:
            print("Please choose valid option")

# Run the program
Menu()

# Close DB connection
cur.close()
con.close()



