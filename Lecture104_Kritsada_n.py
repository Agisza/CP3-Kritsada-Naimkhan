class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " + self.lastName + "'s cart")

customer1 = Customer()
customer1.name = "Bob"
customer1.lastName = "Baby"
customer1.age = 8
customer1.addCart()

customer2 = Customer()
customer2.name = "Poo"
customer2.lastName = "Zii"
customer2.age = 28
customer2.addCart()

customer3 = Customer()
customer3.name = "Oil"
customer3.lastName = "Bam"
customer3.age = 55
customer3.addCart()