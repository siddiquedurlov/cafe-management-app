#Define the menu of restaurant
menu = {
    'Pizza':120,
    'Burger':60,
    'Coffee':40,
    'Shake':80,
}

#Greet

print ("Welcome to Python Restaurant")
print ("Pizza: 120 TK\nBurger: 60 TK\nCoffee : 40 TK\nShake : 80 TK ")

order_total = 0
#120 + 40 = 160

item_1 = input("Enter the name of the item you want to order?=")
if item_1 in menu:
    order_total += menu[item_1] #0 + 40
    print(f"Your item {item_1} has been added to your order.")

else:
    print(f"Orderd item {item_1} is not available!!!")    

another_order = input("Do you want to add more item? (Yes/No)")
if another_order== "Yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")

else:
    print(f"ordered item is not available!!!")

print (f"The total amount of items to pay is {order_total} TK")
