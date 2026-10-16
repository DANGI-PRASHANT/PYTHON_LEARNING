
food_items = []

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
        "status": "Available"
    }

    food_items.append(new_item)
    print("✅ Food item added successfully!")


#  3. VIEW ALL FOOD ITEMS:

def view_food_item():
    if not food_items:
        print("No food items available!")
        return

    print("\n===== FOOD LIST =====")

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
            print(f'Food_ID : {item['Food_ID']}')
            print(f'Item_Name: {item['item_name']}')
            print(f'Category: {item['category']}')
            print(f'Price: {item['price']}')
            print(f"Status: {item['status']}")
            
            found = True
            return
        
    if not found:
        print("❌ Items are not Found\n")
           



# 5. UPDATE FOOD ITEMS:

def update_food_items():
    id = input("Enter Food_ID for Update: ").strip()

    for item in food_items:
        if id.lower() == item["Food_ID"].lower():

            item["item_name"] = input(f"Enter a new_item_name ({item['item_name']}): ")
            item["category"] = input(f"Enter a New_Category ({item['category']}): ")
            item["price"] = input(f"Enter a New_Price (${item['price']}): ")
            print("✅ Successfully Updated!\n")
            return

    print("❌ Invalid ID. Please try again\n")

# 6. DELETE FOOD ITEM

def delete_food_item():
    food_id = input("Enter a Food_ID : ")

    for item in food_items:
        if item["Food_ID"].lower() == food_id.lower():
            food_items.remove(item)
            print("✅ Items deleted successfully!\n")
            return


# 7. CREATE ORDER

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
            "price" : float(input("Enter a Price: ")),
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
    
        print(f"Customer_Name: {item['customer_name']}")
        print(f"Order_ID: {item['order_id']}")
        print(f"Status: {item['status']}")
        print(f"------Items Names----")

        for item in order_items:
            print(f"   {item['food_name']}: {item['quantity']}")


        print(f"Total Order Items: {len(order_items)}")

        print("\n✅ Food item Ordered successfully!\n")
   



# 8. GENERATE BILL

def generate_bill():
    id = input("Enter Order_Id: ")

    found = False
    subtotal = 0
    print("\n========== CUSTOMER BILL ==========")

    for item in order_items:
        if item["order_ID"].lower() == id.lower():
            found = True

            item_total = item['price'] * item['quantity']
            subtotal += item_total

            print(f"\n{item['food_name']}")
            print(f"Quantity: {item['quantity']}")
            print(f"Unit Price: ${item['price']}")
            print(f"Item Total : {item_total}")

    if not found:
        print(f"Invalid Order ID!")

    tax = subtotal * 0.03
    discount = subtotal * 0.1
    Final_total = subtotal - discount + tax

    print("\n---------------------------------")
    print(f"Tax: ${tax}")
    print(f"Discount: ${discount}")
    print(f"Subtotal: ${subtotal}")
    print("----------------------------------")
    print(f"\n===============================")
    print(f"   Final Total: ${Final_total}   ")
    print(f"\n===============================")


# 9. Main Menu

def main_menu():
    while True:
        
        print("\n==========================RESTURANT MANAGEMENT SYSTEM==========================\n")
        print("1.Show Food Menu")
        print("2. Add Food Items")
        print("3. View All Items")
        print("4. Search Food Items")
        print("5. Update Food Items")
        print("6. Delete Food Items")
        print("7. Create New Order and View all Order")
        print("8. Generate Customer Bill")
        print("9. Exit")

        choice = input("\nEnter a number (1 to 10): ")

        if choice == "1":
            food_menu()

        elif choice == "2":
            add_food_items()

        elif choice == "3":
            view_food_item()

        elif choice == "4":
            search_food_items()

        elif choice == "5":
            update_food_items()

        elif choice == "6":
            delete_food_item()

        elif choice == "7":
            create_order()

        elif choice == "8":
            generate_bill()

        elif choice == "10":
            print("Exiting program. Goodbye! 👋")
            break

        else:
            print("❌ Invalid choice. Try again.\n")

# Run the program:

main_menu()

