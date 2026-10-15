
food_items = [
    {"Food_ID":"FD001","item_name": "Chicken Momo", "category": "Snacks", "price": 11.99,"status": "Avaliable"},
    {"Food_ID":"FD002","item_name": "Veg Momo", "category": "Snacks", "price": 9.99,"status": "Avaliable"},
    {"Food_ID":"FD003","item_name": "Dal Bhat", "category": "Main Course", "price": 14.99,"status": "Avaliable"},
    {"Food_ID":"FD004","item_name": "Chicken Curry", "category": "Main Course", "price": 15.99,"status": "Avaliable"},
    {"Food_ID":"FD005","item_name": "Masala Chai", "category": "Drinks", "price": 3.99,"status": "Avaliable"},
    {"Food_ID":"FD006","item_name": "Mango Lassi", "category": "Drinks", "price": 4.99,"status": "Avaliable"},
]

order_items = []

# 1. Food Menu:

def food_menu():
    print("\n======= FOOD MENU =======")

    for number, item in enumerate(food_items, 1):
       
        print(f"{number} . {item["item_name"]} - $ {item["price"]}")



# 2. ADD FOOD ITEMS:

def add_food_items():

    Food_id = input("Enter a Food ID: ").strip()
    item_name = input("Enter an Item Name: ").strip()
    

    if not item_name:
        print("❌ Item name cannot be empty.")
        return

    # Check whether Food_ID already exists
    for item in food_items:
        if item["Food_ID"] == Food_id:
            print("❌ This Food ID already exists!")
            return

    category = input("Enter a Category: ").strip()
    price = input("Enter a Price: ").strip()

    new_item = {
        "Food_ID": Food_id,
        "item_name": item_name,
        "category": category,
        "price": price,
        "Status": "Available"
    }

    food_items.append(new_item)
    print("✅ Food item added successfully!")


#  3. VIEW ALL FOOD ITEMS:

def view_food_item():
    if not food_items:
        print("No food items available!")
        return

    print("\n===== FOOD MENU =====")

    for item in food_items:
        print("Food ID:", item["Food_ID"])
        print("Food Name:", item["item_name"])
        print("Category:", item["category"])
        print("Price: Rs.", item["price"])
        print("Status:",item["status"])
        print("---------------------")


# 4. SEARCH FOOD ITEMS:

def search_food_items():
    food_name = input("Enter a Items Name or Food_ID to search: ")
    found = False

    for item in food_items:
        if food_name.lower() == item["item_name"] or food_name.lower() == item["Food_ID"].lower():
            print("✅ Found it: ")
            print(f'Food_ID : {item["Food_ID"]}')
            print(f'Item_Name: {item["item_name"]}')
            print(f'Category: {item["category"]}')
            print(f'Price: {item["price"]}')
            print(f"Status: {item["status"]}")
            
            found = True
            return
        
    if not found:
        print("❌ Items are not Found\n")
           



# 5. UPDATE FOOD ITEMS:

def update_food_items():
    id = input("Enter Food_ID for Update: ").strip()

    for item in food_items:
        if id.lower() == item["Food_ID"].lower():

            item["item_name"] = input(f"Enter a new_item_name ({item["item_name"]}): ")
            item["category"] = input(f"Enter a New_Category ({item["category"]}): ")
            item["price"] = input(f"Enter a New_Price (${item["price"]}): ")
            print("✅ Successfully Updated!\n")
            return

    print("❌ Invalid ID. Please try again\n")
            

# 7. CREATE ORDER


order_items = []

def create_order():
    
    while True:
        loop_close = input("If you want close(Type a 'Close') otherwise left it : ")

        if loop_close.lower() == "close":
            break 
        
        Order_id = input("Enter a Order ID: ").strip()
        status = input("Enter a Status: ").strip()
        customer_name = input("Enter a Customer_Name: ").strip()
   

        while True:
        
            food_name = input("Enter a Food Name (or 'done' to stop):  ")


            if food_name.lower() == "done":
                break

   
            Quantity = int(input("Enter a Quantity: "))

            Order_Items = {
            "order_id" : str(Order_id),
            "customer_name": customer_name,
            "food_name": str(food_name),
            "quantity" : int(Quantity),
            "status": status,
            }
        
            order_items.append(Order_Items)

        if not food_name:
            print("❌ Food name cannot be empty.")
            return

        # Check whether Order_ID already exists
        for item in order_items:
            if item["order_id"].lower() == Order_id.lower() and  item["customer_name"].lower() == customer_name.lower():
                pass

                if item["food_name"] == food_name:
                    print("❌ This same Order already exists!")
                    return
    
        print(f"Customer_Name: {item["customer_name"]}")
        print(f"Order_ID: {item["order_id"]}")
        print(f"Status: {item["status"]}")
        print(f"------Items Names----")

        for item in order_items:
            print(f"   {item['food_name']}: {item['quantity']}")


        print(f"Total Order Items: {len(order_items)}")
        print("\n✅ Food item Ordered successfully!\n")
   










