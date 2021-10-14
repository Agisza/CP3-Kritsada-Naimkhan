menuList = []

def showBill():
    sumprice = 0
    print("----- My Food-----")
    for nummber in range(len(menuList)):
        sumprice +=  int(menuList[nummber][1])
        print(menuList[nummber][0]," : ",menuList[nummber][1])
    print("ราคารวม :",sumprice)

while True:
    menuName = input("Please Enter Menu:")
    if (menuName.lower()== "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])
showBill()