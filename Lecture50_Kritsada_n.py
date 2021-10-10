def addNumber(x,y):
    print(x+y)
def subNumber(x,y):
    print(x-y)
def mulNumber(x,y):
    print(x*y)
def divNumber(x,y):
    print(x/y)
print("Program Calculate")
print("1. +")
print("2. -")
print("3. x")
print("4. /")
int_selet = input("Select : ")
while int_selet !="1" and int_selet !="2" and int_selet !="3" and int_selet !="4" :
    print("--------Please Select Item 1-4------")
    int_selet = input("Select : ")
x =int(input("X :"))
y =int(input("Y :"))
if int_selet =="1":
    addNumber(x,y)
elif int_selet =="2":
    subNumber(x,y)
elif int_selet =="3":
    subNumber(x,y)
elif int_selet =="4":
    subNumber(x,y)
