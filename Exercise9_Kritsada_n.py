print("---------------Login----------------")
User_Name = input("Username :")
User_Pass = input("Password :")
while User_Name != "admin" or User_Pass != "1234" :
    print("Login Error Please try again")
    User_Name = input("Username :")
    User_Pass = input("Password :")

print("-----Welcome Please Select Item-----")
print("1. Ipad ")
print("2. Ipad Pro ")
print("3. Iphone ")
print("4. Iphone Pro")
print("5. Iphone Pro Max")
print("------------------------------------")

input_key = input("Select : ")
while input_key !="1" and input_key !="2" and input_key !="3" and input_key !="4" and input_key !="5" :
    print("--------Please Select Item 1-5------")
    input_key = input("Select : ")
    print("------------------------------------")

if input_key == "1"   :
    item_name ="Ipad"
    Item_price = 10000
elif input_key == "2" :
    item_name ="Ipad Pro"
    Item_price = 25000
elif input_key == "3" :
    item_name ="Iphone"
    Item_price = 29000
elif input_key == "4" :
    item_name ="Iphone Pro"
    Item_price = 35000
elif input_key == "5" :
    item_name ="Iphone Pro Max"
    Item_price = 45000
print("You select :",item_name)
print("Price : ",Item_price," Baht")
Item_Qty = int(input("How many pieces : ")) 

print("--------------------price summary-------------------")
print("You Buy : ",item_name," Qty : ",Item_Qty," Price : ",Item_Qty*Item_price)
print("----------------------------------------------------")