menuList = []
priceList = []

def showBill():
    sumprice = 0
    print("----- My Food-----")
    for nummber in range(len(menuList)):
        sumprice +=  int(priceList[nummber])
        print(menuList[nummber],priceList[nummber])
    print("ราคารวม :",sumprice)

while True:
    menuName = input("Please Enter Menu:")
    if (menuName.lower()== "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
