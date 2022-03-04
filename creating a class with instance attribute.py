class grocery_list:
    def __init__(self,item,amt):
        self.item=item
        self.amt=amt


customer1=grocery_list("beef",300)
customer2=grocery_list("pepsi",10)
print("cutomer1 bought {} and its amount is {}".format(customer1.item,customer1.amt))
print("cutomer2 bought {} and its amount is {}".format(customer2.item,customer2.amt))