import sqlite3

def init_db():
    conn = sqlite3.connect("onlinefoodordering.db")
    cursor = conn.cursor()

    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS Customer(
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name VARCHAR(20),
            username VARCHAR(20) UNIQUE,
            Password VARCHAR(20),
            email TEXT,
            phone TEXT,
            address TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Food(
            food_id INTEGER PRIMARY KEY AUTOINCREMENT,
            food_name VARCHAR(20),
            food_des TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS [Order](
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            food_id INTEGER,
            price_id INTEGER
        )
    ''')

    conn.commit()
    conn.close()

def register_customer():
    conn = sqlite3.connect("onlinefoodordering.db")
    cursor = conn.cursor()
    username =input("enter your user name: ")
    password = input("enter your password: ")
    name = input("enter your name: ")
    email = input("enter your email id: ")
    phone = input("enter your phone number: ")
    address = input("enter your address: ")

    cursor.execute("SELECT username FROM Customer WHERE username=?",(username,))
    if cursor.fetchone():
       print("username already exists! Try another one.")
    else:
       cursor.execute(
           "INSERT INTO Customer(customer_name,username,password,email,phone,address) VALUES(?,?,?,?,?,?)",
     (name, username, password, email, phone, address)
       )
    conn.commit()
    print("customer registered successfully!")
    conn.close()
def login_customer():
    conn = sqlite3.connect("onlinefoodordering.db")
    cursor =conn.cursor()
    username = input("enter your username")
    password = input("enter your password")
    cursor.execute("SELECT * FROM Customer WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    if user:
           print(f"\nLogin successful! Welcome.")
    else:
        print("Invalid username or password.")
    conn.close()


def search_food():
    conn = sqlite3.connect("onlinefoodordering.db")
    cursor = conn.cursor()

    name = input("Enter food Name to search: ")
    cursor.execute("SELECT * FROM food WHERE food_name Like ?", ('%' + name + '%',))
    data = cursor.fetchall()
    if data:
        print("\n--- Food Items Found ---")
        for item in data:
            print(f"Food ID: {item[0]} -- Name: {item[1]} -- Description: {item[2]}")
    else:
        print("no matching food found.")
    conn.close()
def edit_order():
    conn = sqlite3.connect("onlinefoodordering.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM  [order]" )
    data = cursor.fetchall()
    if data:
        print("\n--- Orders found ---")
        for i in data:
             print(f"Order ID: {i[0]}-- Customer ID: {i[1]} -- Food ID: {i[2]}")
    else:
        print("No orders found.")
    conn.close()

def delete_order():
    conn = sqlite3.connect("onlinefoodordering.db")
    cursor = conn.cursor()
    order_id_input = input("enter the order id to delete: ")
    if  not order_id_input.isdigit():
        print("Invalid ID format. Must be a number.")
        conn.close()
        return
    order_id = int(order_id_input)
    cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
    order = cursor.fetchone()
    if order:
        print("order found")
        print(f"order ID:{order[0]}-- Customer ID: {order[1]}-- Food ID: {order[2]}")
        cursor.execute("DELETE FROM orders WHERE id=?", (order_id,))
        conn.commit()
        print("order deleted successfully!")
    else:
         print("no order found")
    conn.close()

def main():
    init_db()
    print("ONLINE FOOD ORDERING")

    while True:
        print("\n1. Register Customer")
        print("2. Login Customer")
        print("3. Search Food")
        print("4. Edit Order")
        print("5. Delete Order")
        print("6. Exit")

        user_input = input("Enter your choice: ")

        if user_input.isdigit():
            ch = int(user_input)

            if ch == 1:
               register_customer()
            elif ch == 2:
                 login_customer()
            elif ch == 3:
                 search_food()
            elif ch == 4:
                 edit_order()
            elif ch == 5:
                 delete_order()
            elif ch == 6:
                print("Exiting system.")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid input. Please enter a valid number.")
if __name__ == "__main__":
    main()










