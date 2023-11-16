1
import valid
import random
from tabulate import tabulate
class C_signup:
    def __init__(self):
        self.cus_details={}     #empty dictionary to store list customer details
        self.shop_cart={}
    def signup(self):
        id_details=[]           #empty list to store customer details
        print("("+"*"*11+"Please Enter the following details"+"*"*11+")\n")
        print("="*28,"\nAvailable Locations are:\n"+"="*28)
        print(" "*6,"Adyar\n"," "*5,"Besant nagar\n"," "*5,"Indira nagar\n"," "*5,"T-nagar\n")
        while True:
            location=input("Please Choose Location :").lower()
            if location=="adyar" or location=="besant nagar" or location=="indira nagar" or location=="t-nagar":
                break
            else:
                print("Entered Location not available.Please enter nearest location")
        while True:
            c_name=input('Enter your Name :')
            if valid.name_validation(c_name):
                break
        while True:
            c_phone_number=input('Enter the phone no. :')
            if valid.phone_number_validation(c_phone_number):
                break
        locations={'adyar':"Ad",'besant nagar':'Bn','indira nagar':'In','t-nagar':'Tn'}
        if location in locations:
            last=locations[location]
        ran_phnum=random.sample(c_phone_number,4)       #generating customer id by the phone number
        phnId=''        
        self.c_id='abc'+(phnId.join(ran_phnum))+last
        print('Your customer ID is ',self.c_id)         #appending every details of customer into the id_details list
        id_details.append(c_name)
        id_details.append(c_phone_number)
        id_details.append(location)
        self.cus_details[self.c_id]=id_details          #updating the dictionary with value of id_details with the customer id as the key
        print('\nHELLO ',c_name.upper())
class ShoppingCart(C_signup):
    def __init__(self):
        super().__init__()
    def avail_item(self):
        while True:
            entd_customer=input("Enter customer's id :")
            if entd_customer in self.cus_details:
                break
            else:
                print('Incorrect customer ID')
        print('\nAdd Products to the cart!\n')
        items={}        #empty dict to store available items
        self.slctd_items=[] #empty list to store selected items
        self.prices=[]  #empty list to store the price of the selected items
        items.update([('1.Milk',150),('2.Bread',99),('3.Eggs',150)])
        keys=list(items.keys()) #creating list with the keys of the available items dictionary to select the product according to the index
        f=1
        while True:
            item_data = [[key, value] for key, value in items.items()] #converting dict into list
            print(tabulate(item_data, headers=["items", "price"], tablefmt="grid"))
            while True:
                ind=input('Enter item number to add to cart(press ''q'' to quit) :')
                if ind.isdigit():# and int(ind)>0:
                    if int(ind)<=len(items):
                        break
                    else:
                        print('Please enter choice within available items')
                        continue
                elif ind=='Q' or ind=='q':
                    print('discounted products are available..')
                    while True:
                        dscn=input('Do you want to purchase(y/n) :').lower()
                        if valid.decision(dscn):
                            break
                    if dscn=="y":
                        self.discount_prod()
                        break
                    elif dscn=='n':
                        break
                    #f=0
                    break
                else:
                    print('please enter only available item number or q to quit')
                    continue
                break
            while True:
                try:
                    quantity=float(input('Enter quantity :'))
                    if valid.valid_quantity(quantity):
                        break
                except ValueError:
                   print('please enter numerical values')
            item=keys[int(ind)-1]   #storing the selected item into the (item) variable using the indexing method 
            if item in self.slctd_items:    #checking whether the selected item is been already selected
                for count,value in enumerate(self.slctd_items): #if already selected item is selected again then chnging price alone for that item
                    if value==item:
                        self.prices[count]+=(items[item]*quantity)  #updating the price for reselected item
                        print(item,'updated.now the price is,',self.prices[count])
            else:
                self.slctd_items.append(item)   #appending the selected item in list of selected items
                price=(items[item]*quantity)    #calculating for total price of the selected item
                self.prices.append(price)       #appending the total price of the selected item in prices list
                    
class Discount(ShoppingCart):
    def __init__(self):
        super().__init__()
        self.disply_items=[]
    def discount_prod(self):
        discount_products=['Sugar','Sugar','Rice','Rice','Atta','Atta']
        discount_products_price=['1kg','5kg','10kg','25kg','5kg','10kg']
        discount=['5%','10%','4%','8%','6%','12%']
        discounts=zip(discount_products,discount_products_price,discount)
        print(tabulate(discounts,headers=['PRODUCTS','QUANTITY','DISCOUNT'],tablefmt="double_outline"))
        print("List of available items for shopping")
        d_items={'Sugar':40,'Rice':50,'Atta':60}
        keys=list(d_items.keys())
        item_data = [[key, value] for key, value in d_items.items()] #converting dict into list
        while True: 
            print(tabulate(item_data,headers=['PRODUCTS','PRICE'],tablefmt="grid"))
            ind=input('Enter item number to add to cart(press ''q'' to quit) :')
            if ind=="Q" or ind=="q":
                break
            elif ind.isdigit() and int(ind)>0:
                while True:
                    if int(ind)<=len(d_items):
                        break
                    else:
                        print('Please enter choice within available items')
                while True:
                    try:
                        quantity=int(input('Enter quantity :'))
                        if valid.valid_quantity(quantity):
                            break
                    except ValueError:
                           print('please enter numerical values')
                item=keys[int(ind)-1]
                if item in self.slctd_items:        #checking whether the selected item is been already selected
                    for count,value in enumerate(self.slctd_items):
                        if value==item:
                            self.prices[count]+=(d_items[item]*quantity)
                            if item=='Sugar':       #calcualting the price after the discount according to the selected item
                                if quantity<5:
                                    disc_amount=(d_items[item]*quantity)*.05
                                    self.prices[count]-=disc_amount
                                else:
                                    disc_amount=(d_items[item]*quantity)*.1
                                    self.prices[count]-=disc_amount
                            if item=='Rice':
                                if quantity<10:
                                    disc_amount=(d_items[item]*quantity)*.04
                                    self.prices[count]-=disc_amount
                                else:
                                    disc_amount=(d_items[item]*quantity)*.08
                                    self.prices[count]-=disc_amount
                            if item=='Atta':
                                if quantity<5:
                                    disc_amount=(d_items[item]*quantity)*.06
                                    self.prices[count]-=disc_amount
                                else:
                                    disc_amount=(d_items[item]*quantity)*.12
                                    self.prices[count]-=disc_amount
                            print(item,'updated.now the price is,',self.prices[count])
                else:
                    self.slctd_items.append(item)
                    price=(d_items[item]*quantity)  #calculating the total price for selected item
                    if item=='Sugar':       #subtracting the value of dicounted amount according to the product 
                        if quantity<5:
                            price-=price*.05        
                        else:
                            price-=price*.1
                    elif item=='Rice':
                        if quantity<10:
                            price-=price*.04
                        else:
                            price-=price*.08
                    elif item=='Atta':
                        if quantity<5:
                            price-=price*.06
                        else:
                            price-=price*.12
                    self.prices.append(price)       
                    print(item,'added to the cart.Total price Rs.',price)
            else:
                print('please enter only available item number or (q) to quit')
    def reciept(self):
        print("="*28,"\nAvailable Delivery Locations are:\n"+"="*28)
        print(" "*6,"Adyar\n"," "*5,"Besant nagar\n"," "*5,"Indira nagar\n"," "*5,"T-nagar\n")
        avail_locations=['adyar','Besant nagar','Indira nagar','t-nagar']
        while True:
            deli_location=input('Enter delivery location :').lower()
            if deli_location.isalpha():
                if deli_location in avail_locations:
                    break
                else:
                    print('Sorry, online delivery is not available.')
            else:
                print('location should be in alphabet')
        ch=input('\nwould you like to pick it up from our nearest store(y/n) :').lower()
        if ch=='n':
            print('Delivery charges will be applied\n')
            self.slctd_items.append('delivery charges')     #appending the delivery charges into the selected items list
            self.prices.append(20)
        tot=sum(self.prices)    #calculating the total amount by using sum function in prices list
        self.slctd_items.append('Total amount')
        self.prices.append(tot)     #appending the total amount into the list to print
        self.disply_items = zip(self.slctd_items,self.prices)   #combining the prodct list and prices list
        self.shop_cart[self.c_id]=self.disply_items
        print('\nCustomer Name :',list(self.cus_details.values())[0][0])      #printing the customer detail by slicing the values of cus_details dictionary
        print('\nCustomer Id :',self.c_id)
        print('\nCustomer Phone no :',list(self.cus_details.values())[0][1])
        print('\nCustomer Location :\n',list(self.cus_details.values())[0][2])
        print(tabulate(self.disply_items,headers=['Item Name','Price'],tablefmt='grid'))
class LuckyDraw(Discount):
    def __init__(self):
        super().__init__()
    def register_luckydraw(self):
        print('\nWelcome to lucky draw\n')
        while True:
            luck_c_id=input("Enter customer's ID :")        #getting input for customer id to check whether the customer is already registered or not
            if luck_c_id in self.cus_details:
                break
            else:
                print('Please enter registered customer id')
        while True:
            self.luck_name=input('Enter customer name :')
            if valid.name_validation(self.luck_name):
                break
        while True:
            luck_location=input('Enter customer location :')
            if luck_location=="adyar" or luck_location=="besant nagar" or luck_location=="indira nagar" or luck_location=="t-nagar":
                break
            else:
                print("Entered Location not available.")
    def luckydraw(self):
        print((self.luck_name).upper())
        print('\nNow its time to spin the board...\nAnd the result is...')
        coupons=['NEW SMARTPHONE','NEW HELMET','NEW COOKWARE','FLAT 200','better luck next time']
        slctd_coupon=random.choice(coupons)     #random module used to choose the coupon
        if slctd_coupon!='better luck next time':
            print('\n\nCongratulations!You have won a',slctd_coupon)
        else:
            print('Sorry!',slctd_coupon)
        print('\nThank you for shopping with us and participating in the Lucky Draw.Have a great day!\n')
s1=LuckyDraw()        
while True:
    print('\n'+"~"*20+'Welcome to the Abc online Supermarket'+'~'*20)
    print('\n'*2,'\t1)Sign up(New user)\n\t2)Sign in\n\t3)exit\n')
    choice=input('Enter Your Choice :')
    if choice=='1':
        s1.signup()
    elif choice=='2':
        if len(s1.cus_details)>0:
            s1.avail_item()
            s1.reciept()
            s1.register_luckydraw()
            s1.luckydraw()
        else:
            print('You\'re not registered. please signup before login')
        
    elif choice=='3':
        print('Exiting the application...')
        break
    else:
        print('please enter valid choice')
