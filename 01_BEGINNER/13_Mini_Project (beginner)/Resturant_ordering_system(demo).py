print("======RESTAURANT ORDERING SYSTEM=======")

have = input(" (Sign in / Continu as guest):")

if have.lower() == "sign in":


    username = input("Enter Username:")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":
        print("Login successfull")

        buy= input("Do you want to buy something? (yes/no):")
        if buy == "yes":
                print("----------> MENU <-----------")
                print("""
                Burger🍔 : $8
                Pizza🍕 : $12
                Sandwich🥪: $6
                """)
        
                Burger = int(input("How many burger do you want:"))
                Pizza = int(input("How many pizza do you want: "))
                sandwich = int(input("How many sandwich do you want:"))
        
                price1 = Burger *8
                price2 = Pizza *12
                price3 = sandwich*6
        
        
                total_price = price1 + price2 +price3
                print(f"Total amount:${total_price}")
        
                if total_price >= 50:
                    dis = total_price *0.2
                    print(f"Discount: ${dis}")
                    print(f"Final Total: ${total_price - dis}")
                
                elif total_price >=30:
                    dis = total_price *0.1
                    print(f"Discount: ${dis}")
                    print(f"Final total:${total_price-dis}")
                
                else: 
                    print("No discount.")
                    print(f"Final Total: ${total_price}")
        
        
                    
        
              
            
                deli = input("Do you want delivery? (yes/no): ")
        
                if deli == "yes":
                    print("Delivery cost is $5.")
        
                    location = input("Enter your location: ")
                    print("                             Your order is Ready.                                ")
                    print("                             The Delivery-man call before a delivery.             ")
                    print("                             THANKS FOR CHOOSING US                              .")
                    print("                             ORDER SUCCESSFULL                                   ")
        
                elif deli == "no" :
                # print("No delivery")
                    print("                             THANKS FOR CHOOSING US                            .")
                    print("                             ORDER SUCCESSFULL                                  ")
            
                else:
                    print("Invalid delivery option.")
        else:
              print("Thanks for visiting☺️")

elif have.lower() == "continu as guest":

    buy= input("Do you want to buy something? (yes/no):")
    
    
    if buy == "yes":
        print("----------> MENU <-----------")
        print("""
            Burger🍔 : $8
            Pizza🍕 : $12
            Sandwich🥪: $6
            """)
    
        Burger = int(input("How many burger do you want:"))
        Pizza = int(input("How many pizza do you want: "))
        sandwich = int(input("How many sandwich do you want:"))
    
        price1 = Burger *8
        price2 = Pizza *12
        price3 = sandwich*6
    
    
        total_price = price1 + price2 +price3
        print(f"Total amount:{total_price}")
    
        if total_price >= 50:
                dis = total_price *0.2
                print(f"Discount: ${dis}")
                print(f"Final Total: ${total_price - dis}")
            
        elif total_price >=30:
                dis = total_price *0.1
                print(f"Discount: ${dis}")
                print(f"Final total:${total_price-dis}")
            
        else: 
                print("No discount.")
                print(f"Final Total: ${total_price}")
    
    
                
    
            
        
        deli = input("Do you want delivery? (yes/no): ")
    
        if deli == "yes":
                print("Delivery cost is $5.")
    
                location = input("Enter your location: ")
                print("                             Your order is Ready.                                ")
                print("                             The Delivery-man call before a delivery.             ")
                print("                             THANKS FOR CHOOSING US                              .")
                print("                             ORDER SUCCESSFULL                                   ")
    
        elif deli == "no" :
            # print("No delivery")
                print("                             THANKS FOR CHOOSING US                              .")
                print("                             ORDER SUCCESSFULL                                   ")
        
        else:
                print("Invalid delivery option.")
    else:
          print("Thanks for visting☺️")
else:
      print('Invalid')
    