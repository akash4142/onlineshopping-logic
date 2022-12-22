jeanlist=["1. bell bottoms    1900 ruppee","2. patchwork    2000 ruppee","3. acid wash    2500 ruppee","4. flared    1700 ruppee","5.bootcut      1900 ruppee"]
print("Welcome to akash online shopping app")
str1=input("Enter your name :: ")
i=1
while i<=3:
    print(str1,"choose your category :: ")
    print("press 1 for clothes\npress 2 for electronics\npress 3 for perfumes\npress 4 for shoes\n5 for mobile phones")
    choice=int(input("tell us your choice :: "))
    if choice==1:
        print("welcome to the clothing section")
        print("choose the cloth type :: ")
        print("1 for jeans\n2 for shirts\n3 for tshirt\n4 for trackpants")
        cloth=int(input())
        if cloth==1:
            print("*****WELCOME  YOU HAVE ENTERED INTO THE JEANS SECTION*****")
            print("here is the list of jeans available :: ")
            for i in jeanlist:
                print(jeanlist)
                num=int(input("enter your choice :: "))
                print("are you sure you want to place order \n 1 for yes \n 2 for no ")
                num1=int(input())
                if num1==1:
                        print("How would you like to pay :: \n 1 for cash on delievery\n 2 for credit card ")
                num2=int(input())
                if num2==1:
                        print("Thank you . Your order is placed . Thank you for your our services")
                        i=i+1
                elif num2==2:
                    credit=int(input("enter your credit card number ::"))
                    password=int(input("enter your password :: "))
                    
                
                
            

        elif cloth==2:
            print("*****WELCOME  YOU HAVE ENTERED INTO THE shirt SECTION*****")
            print("here is the list of shirts available :: ")
            print("1. full seelves  red 900 ruppee\n2. red shirt   200 ruppee\n3. black shirt  500 ruppee\n4. blue shirt    700 ruppee\n5.black shirt     900 ruppee")
            num=int(input("enter your choice :: "))
            print("are you sure you want to place order \n 1 for yes \n 2 for no")
            num1=int(input())
            if num1==1:
                print("How would you like to pay :: \n 1 for cash on delievery\n 2 for credit card")
                num2=int(input())
                if num2==1:
                    print("Thank you . Your order is placed . Thank you for your our services")
                    i=i+1
                elif num2==2:
                    credit=int(input("enter your credit card number ::"))
                    password=int(input("enter your password :: "))
                

        elif cloth==3:
            print("*****WELCOME  YOU HAVE ENTERED INTO THE tshirt SECTION*****")
            print("here is the list of tshirts available :: ")
            print("1. full seelves  red 900 ruppee\n2. red tshirt   200 ruppee\n3. black tshirt  500 ruppee\n4. blue tshirt    700 ruppee\n5.black tshirt     900 ruppee")
            num=int(input("enter your choice :: "))
            print("are you sure you want to place order \n 1 for yes \n 2 for no")
            num1=int(input())
            if num1==1:
                print("How would you like to pay :: \n 1 for cash on delievery\n 2 for credit card")
                num2=int(input())
                if num2==1:
                    print("Thank you . Your order is placed . Thank you for your our services")
                    i=i+1
                elif num2==2:
                    credit=int(input("enter your credit card number ::"))
                    password=int(input("enter your password :: "))
                



        elif cloth==4:
            print("*****WELCOME  YOU HAVE ENTERED INTO THE trackpants SECTION*****")
            print("here is the list of trackpants available :: ")
            print("1. red trackpant 1900 ruppee\n2. navy blue trackpant   1200 ruppee\n3. black trackpant  1500 ruppee\n4. blue trackpant    1700 ruppee\n5.black trackpant    1900 ruppee")
            num=int(input("enter your choice :: "))
            print("are you sure you want to place order \n 1 for yes \n 2 for no")
            num1=int(input())
            if num1==1:
                print("How would you like to pay :: \n 1 for cash on delievery\n 2 for credit card")
                num2=int(input())
                if num2==1:
                    print("Thank you . Your order is placed . Thank you for your our services")
                    i=i+1
                elif num2==2:
                    credit=int(input("enter your credit card number ::"))
                    password=int(input("enter your password :: "))
        else:
            print("wrong input")
    elif choice==2:
        print("welcome to the electronics section")
        print("choose the electronics type :: ")
        print("1 for A.C\n2 for L.C.D")
        electronics=int(input())
        if electronics==1:
            print("*****WELCOME  YOU HAVE ENTERED INTO THE A.C SECTION*****")
            print("here is the list of A.C available :: ")
            print("1. whirlpool    27000 ruppee\n2. voltas    30000 ruppee\n3. bluestar    25000 ruppee\n4. mitsubishi    17000 ruppee\n5.panasonic      19000 ruppee")
            num=int(input("enter your choice :: "))
            print("are you sure you want to place order \n 1 for yes \n 2 for no")
            num1=int(input())
            if num1==1:
                print("How would you like to pay :: \n 1 for cash on delievery\n 2 for credit card")
                num2=int(input())
                if num2==1:
                    print("Thank you . Your order is placed . Thank you for your our services")
                    i=i+1
                elif num2==2:
                    credit=int(input("enter your credit card number ::"))
                    password=int(input("enter your password :: "))
                




        elif electronics==2:
            print("*****WELCOME  YOU HAVE ENTERED INTO THE L.C.D SECTION*****")
            print("here is the list of L.C.D available :: ")
            print("1. lampo    27000 ruppee\n2. samsung   30000 ruppee\n3. realme    25000 ruppee\n4. red mi    17000 ruppee\n5.panasonic      19000 ruppee")
            num=int(input("enter your choice :: "))
            print("are you sure you want to place order \n 1 for yes \n 2 for no")
            num1=int(input())
            if num1==1:
                print("How would you like to pay :: \n 1 for cash on delievery\n 2 for credit card")
                num2=int(input())
                if num2==1:
                    print("Thank you . Your order is placed . Thank you for your our services")
                    i=i+1
                elif num2==2:
                    credit=int(input("enter your credit card number ::"))
                    password=int(input("enter your password :: "))

        else:
            print("wrong input")
    elif choice==3:
        print("welcome to the perfume section")
        print("choose the perfume company :: ")
        print("1 for wildstone\n2 for fogg\n3 for axe")
        num=int(input("enter your choice :: "))
        print("are you sure you want to place order \n 1 for yes \n 2 for no")
        num1=int(input())
        if num1==1:
            print("How would you like to pay :: \n 1 for cash on delievery\n 2 for credit card")
            num2=int(input())
            if num2==1:
                print("Thank you . Your order is placed . Thank you for your our services")
                i=i+1
            elif num2==2:
                credit=int(input("enter your credit card number ::"))
                password=int(input("enter your password :: "))
                


    elif choice==4:
        print("welcome to the shoes section")
        print("choose the shoes company :: ")
        print("1 for nike\n2 for adidas\n3 for campus\n4 for sega \n5 for gucci")
        shoes=int(input())
        if shoes==1:
            print("*****WELCOME  YOU HAVE ENTERED INTO THE NIKE SECTION*****")
            print("here is the list of shoes available :: ")
            print("1. nike jordan   1900 ruppee\n2. nike air force 1    2000 ruppee\n3. nike air   2500 ruppee")
            num=int(input("enter your choice :: "))
            print("are you sure you want to place order \n 1 for yes \n 2 for no")
            num1=int(input())
            if num1==1:
                print("How would you like to pay :: \n 1 for cash on delievery\n 2 for credit card")
                num2=int(input())
                if num2==1:
                    print("Thank you . Your order is placed . Thank you for your our services")
                    i=i+1
                elif num2==2:
                    credit=int(input("enter your credit card number ::"))
                    password=int(input("enter your password :: "))
                

        elif shoes==2:
            print("*****WELCOME  YOU HAVE ENTERED INTO THE ADIDAS SECTION*****")
            print("here is the list of shoes available :: ")
            print("1. adidas jordan   1900 ruppee\n2. adidas air force 1    2000 ruppee\n3. adidas air   2500 ruppee")
            num=int(input("enter your choice :: "))
            print("are you sure you want to place order \n 1 for yes \n 2 for no")
            num1=int(input())
            if num1==1:
                print("How would you like to pay :: \n 1 for cash on delievery\n 2 for credit card")
                num2=int(input())
                if num2==1:
                    print("Thank you . Your order is placed . Thank you for your our services")
                    i=i+1
                elif num2==2:
                    credit=int(input("enter your credit card number ::"))
                    password=int(input("enter your password :: "))
                


        elif shoes==3:
            print("*****WELCOME  YOU HAVE ENTERED INTO THE CAMPUS SECTION*****")
            print("here is the list of shoes available :: ")
            print("1. campus jordan   1900 ruppee\n2. campus air force 1    2000 ruppee\n3. campus air   2500 ruppee")
            num=int(input("enter your choice :: "))
            print("are you sure you want to place order \n 1 for yes \n 2 for no")
            num1=int(input())
            if num1==1:
                print("How would you like to pay :: \n 1 for cash on delievery\n 2 for credit card")
                num2=int(input())
                if num2==1:
                    print("Thank you . Your order is placed . Thank you for your our services")
                    i=i+1
                elif num2==2:
                    credit=int(input("enter your credit card number ::"))
                    password=int(input("enter your password :: "))
                

        elif shoes==4:
            print("*****WELCOME  YOU HAVE ENTERED INTO THE SEGA SECTION*****")
            print("here is the list of shoes available :: ")
            print("1. sega jordan   1900 ruppee\n2. sega air force 1    2000 ruppee\n3. sega air   2500 ruppee")
            num=int(input("enter your choice :: "))
            print("are you sure you want to place order \n 1 for yes \n 2 for no")
            num1=int(input())
            if num1==1:
                print("How would you like to pay :: \n 1 for cash on delievery\n 2 for credit card")
                num2=int(input())
                if num2==1:
                    print("Thank you . Your order is placed . Thank you for your our services")
                    i=i+1
                elif num2==2:
                    credit=int(input("enter your credit card number ::"))
                    password=int(input("enter your password :: "))
                

        elif shoes==5:
            print("*****WELCOME  YOU HAVE ENTERED INTO THE GUCCI SECTION*****")
            print("here is the list of shoes available :: ")
            print("1. gucci jordan   1900 ruppee\n2. gucci air force 1    2000 ruppee\n3. gucci air   2500 ruppee")
            num=int(input("enter your choice :: "))
            print("are you sure you want to place order \n 1 for yes \n 2 for no")
            num1=int(input())
            if num1==1:
                print("How would you like to pay :: \n 1 for cash on delievery\n 2 for credit card")
                num2=int(input())
                if num2==1:
                    print("Thank you . Your order is placed . Thank you for your our services")
                    i=i+1
                elif num2==2:
                    credit=int(input("enter your credit card number ::"))
                    password=int(input("enter your password :: "))
                

        else:
            print("wrong input")
    elif choice==5:
        print("welcome to the mobile phones section")
        print("choose the mobile phones type :: ")
        print("1 for android \n2 for iphone")
        phone=int(input())
        if phone==1:
            print("*****WELCOME  YOU HAVE ENTERED INTO THE Android SECTION*****")
            print("here is the list of Android phones available :: ")
            print("1.samsung s1   27000 ruppee\n2.real me 7    10000 ruppee\n3.redmi note 7   14000 ruppee\n4.redmi note 10   20000 ruppee\n5.oppo a1      19000 ruppee")
            num=int(input("enter your choice :: "))
            print("are you sure you want to place order \n 1 for yes \n 2 for no")
            num1=int(input())
            if num1==1:
                print("How would you like to pay :: \n 1 for cash on delievery\n 2 for credit card")
                num2=int(input())
                if num2==1:
                    print("Thank you . Your order is placed . Thank you for your our services")
                    i=i+1
                elif num2==2:
                    credit=int(input("enter your credit card number ::"))
                    password=int(input("enter your password :: "))
                

        elif phone==2:
            print("*****WELCOME  YOU HAVE ENTERED INTO THE iphone SECTION*****")
            print("here is the list of i phones available :: ")
            print("1. i phone 6s  14000 ruppee\n2. i phone 10    27000 ruppee\n3. i phone 11   50000 ruppee")
            num=int(input("enter your choice :: "))
            print("are you sure you want to place order \n 1 for yes \n 2 for no")
            num1=int(input())
            if num1==1:
                print("How would you like to pay :: \n 1 for cash on delievery\n 2 for credit card")
                num2=int(input())
                if num2==1:
                    print("Thank you . Your order is placed . Thank you for your our services")
                elif num2==2:
                    credit=int(input("enter your credit card number ::"))
                    password=int(input("enter your password :: "))
                

        else:
            print("wrong input")
