def login():
    print("----- login -----")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("Login Try Again")
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()

def menuSelect():
    inp_select = int(input(">>"))
    if inp_select == 1 :
        price_vat = int((input("Price :")))
        print(vatCalculator(price_vat))
        ext()
    elif inp_select == 2 :
        print(priceCalculator())
        ext()
    else :
        print("Please Select 1-2")
        menuSelect()

def vatCalculator(totalPrice):
    result = 0
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

def ext() :   
    ex = input("Continue (Y/N) :")
    if ex == "y" or ex == "Y" :
        showMenu()
    else :
        exit()

login()    



