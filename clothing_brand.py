# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:20:33 2020

@author: DELL
"""


#CLOTHING BRAND
#PROJECT

import csv
import random
shopping_cart={}

print('\x1b[6;31;46m' + "\n\t\t\tWELCOME TO DROP CLOTHING" + '\x1b[0m')
print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~")
print("\nThe following brands are availabe to shop from!:\n")
print("1:NIKE")
print("2:ADIDAS")
print("3:PUMA")
print("4:LEVI'S")
print("OR:")
print("5:PPROCEED TO CHECK OUT")
print("0:TO EXIT")

def robot(): 
    a=random.randint(10000,99999)
    print("\nThe confirmation number is:",a)
    n=int(input("To Confirm you are not a robot,please type the above number="))
    if a==n:
       print("Access Granted")
    else:
        print("Access Denied")
        print("Try again")
        robot()
robot()


# nike
def Nike():
    print('\n\x1b[0;34;46m' + "Just Do It" + '\x1b[0m')
    print("Welcome to the Nike store")
    print("The following is the 2020 apparel:")
    d={1:("Nike HyperCharge 24oz Water Bottle",399),
       2:("Nike Printed Backpack with Adjustable Shoulder Straps",1999),
       3:("Nike Logo Print T-Shirt Green",1899),
       4:("Nike Mens Running Shorts",999)}
    l=d.keys()
    print("\nSlNo.\t\t","Item\t\t","\t\tPrice(Rs)")
    for i in l:
        z=d[i]
        print("\n",i,"\t\t",end="")
        for j in z:
            print(j,"\t\t",end="\t\t")
    n=int(input("\nEnter the serial number of item you wish to purchase:"))
    if n==1:
        shopping_cart['Nike HyperCharge 24oz Water Bottle']=399
        print("Nike HyperCharge 24oz Water Bottle Added")
    elif n==2:
        shopping_cart['Nike Printed Backpack with Adjustable Shoulder Straps']=1999
        print("Nike Printed Backpack with Adjustable Shoulder Straps Added")
    elif n==3:
        shopping_cart['Nike Logo Print T-Shirt Green']=1899
        print("'Nike Logo Print T-Shirt Green Added")
    elif n==4:
        shopping_cart["Nike Men's Running Shorts"]=999
        print("Nike Men's Running Shorts Added")

# adidas
def Adidas():
    print('\n\x1b[0;34;46m' + "Impossible Is Nothing" + '\x1b[0m')
    print("Welcome to the Adias store")
    print("The following is the 2020 apparel:")
    d={1:("Adidas steel straw 600 ML metal bottle",999),
       2:("Adidas Originals Striped Backpack",3999),
       3:("Adidas Baseball Lightweight Cap",750),
       4:("Adidas Tricolour Tshirt",1999)}
    l=d.keys()
    print("\nSlNo.\t\t","Item\t\t","\t\tPrice(Rs)")
    for i in l:
        z=d[i]
        print("\n",i,"\t\t",end="")
        for j in z:
            print(j,"\t\t",end="\t\t")
    n=int(input("\nEnter the serial number of item you wish to purchase:"))
    if n==1:
        shopping_cart['Adidas steel straw 600 ML metal bottle']=999
        print("Adidas steel straw 600 ML metal bottle Added")
    elif n==2:
        shopping_cart['Adidas Originals Striped Backpack']=3999
        print("Adidas Originals Striped Backpack Added")
    elif n==3:
        shopping_cart['Adidas Baseball Lightweight Cap']=750
        print("Adidas Baseball Lightweight Cap Added")
    elif n==4:
        shopping_cart['Adidas Tricolour Tshirt']=1999    
        print("Adidas Tricolour Tshirt Added")

# puma
def Puma():
    print('\n\x1b[0;34;46m' + "Forever Faster" + '\x1b[0m')
    print("Welcome to the Puma store")
    print("The following is the 2020 apparel:")
    d={1:("Puma Printed Hoodie with Long Sleeves",2499),
       2:("Puma mens's Sweatpants Cotton Black",1399),
       3:("Puma Snapback Hat",749),
       4:("PUMA Smartwatch",19999)}
    l=d.keys()
    print("\nSlNo.\t\t","Item\t\t","\t\tPrice(Rs)")
    for i in l:
        z=d[i]
        print("\n",i,"\t\t",end="")
        for j in z:
            print(j,"\t\t",end="\t\t")
    n=int(input("\nEnter the serial number of item you wish to purchase:"))
    if n==1:
        shopping_cart['Puma Printed Hoodie with Long Sleeves']=2499
        print("Puma Printed Hoodie with Long Sleeves Added")
    elif n==2:
        shopping_cart["Puma mens's Sweatpants Cotton Black"]=1399
        print("Puma mens's Sweatpants Cotton Black Added")
    elif n==3:
        shopping_cart['Puma Snapback Hat']=749
        print("Puma Snapback Hat Added") 
    elif n==4:
        shopping_cart['PUMA Smartwatch']=19999    
        print("PUMA Smartwatch Added") 

# Levi's
def Levi():
    print('\n\x1b[0;34;46m' + "Quality never goes out of style" + '\x1b[0m')
    print("Welcome to the Levi's store")
    print("The following is the 2020 apparel:")
    d={1:("Classic Denim Baseball Hat",599),
       2:("Slim Fit Levi’s Flex Women's Jeans",2999),
       3:("Levi's Graphic Pullover Hoodie",2750),
       4:("Levi's Vintage Jean Jacket",4999)}
    l=d.keys()
    print("\nSlNo.\t\t","Item\t\t","\t\tPrice(Rs)")
    for i in l:
        z=d[i]
        print("\n",i,"\t\t",end="")
        for j in z:
            print(j,"\t\t",end="\t\t")
    n=int(input("\nEnter the serial number of item you wish to purchase:"))
    if n==1:
        shopping_cart['Classic Denim Baseball Hat']=599
        print("Classic Denim Baseball Hat Added")
    elif n==2:
        shopping_cart["Slim Fit Levi’s Flex Women's Jeans"]=2999
        print("Slim Fit Levi’s Flex Women's Jeans Added")
    elif n==3:
        shopping_cart["Levi's Graphic Pullover Hoodie"]=2750
        print("Levi's Graphic Pullover Hoodie Added")
    elif n==4:
        shopping_cart["Levi's Vintage Jean Jacket"]=4999    
        print("Levi's Vintage Jean Jacket Added")

# check out
def CheckOut():
    with open('billing.csv', 'w') as f:
        for key in shopping_cart:
            f.write("%s,%s\n"%(key,shopping_cart[key]))
        f.flush()
    print('\n\x1b[0;34;46m' + "Your bill is:" + '\x1b[0m')
    #print("Your bill is:")
    print("\tITEM \t\t\t\t        PRICE")
    Csvfile=open("billing.csv","r",newline="")
    Csvobj=csv.reader(Csvfile)
    for line in Csvobj:
        print(line)
    
    total=0
    price=shopping_cart.values()
    for i in price:
        total=total+int(i)
    #print("Your total is:",total)
    print('\n\x1b[0;37;41m' + "Your total is:" + '\x1b[0m',total)
    
    
    payment_method=str(input("How would u like to pay:(CARD/CASH)?:"))
    new_payment_method=payment_method.lower()
    if new_payment_method=="card":
        print("You choose card")
        int(input("Enter credit card number:"))
        condition1=str(input("Would you like to provide us feedback to imporve our service(Yes/no):"))
        new_condition=condition1.upper()
        if new_condition=="YES":
            feedback()
        else:
            print("Thanking you shopping.Please visit soon")
    elif new_payment_method=="cash":
        print("You choose cash")
        condition1=str(input("Would you like to provide us feedback to imporve our service(Yes/no):"))
        new_condition=condition1.upper()
        if new_condition=="YES":
            feedback()
        else:
            print("Thanking you shopping.Please visit soon")
            

    else:
        print("Please type the correct input")
        CheckOut()

# feedback
def feedback():
    with open("FEEDBACK.csv",'a',newline="") as Csvfile:
        Csvobj=csv.writer(Csvfile)
        line=[]
        Name=str(input("Please enter your name:"))
        Rating=float(input("Please rate the customer service(out of 10):"))
        Suggestion=str(input("Any suggestions to enhance your shopping experience:"))
        line=[Name,Rating,Suggestion]
        Csvobj.writerow(line)
        print("Thank you for shopping with us!")
        Csvfile.flush()                                

# menu
while True:
    print("\n1:NIKE,2:ADIDAS,3:PUMA,4:LEVI'S")
    print("OR:5:PPROCEED TO CHECK OUT,0:TO EXIT")
    choice=str(input("Please select a brand to shop,proceed to checkout,or exit:"))
    if choice=="1":
        Nike()
    elif choice=="2":
        Adidas()
    elif choice=="3":
       Puma()
    elif choice=="4":
        Levi()
    elif choice=="5":
       CheckOut()
    elif choice=="0":
        break
    else:
        print("Wrong choice")
print("End of runtime")   













