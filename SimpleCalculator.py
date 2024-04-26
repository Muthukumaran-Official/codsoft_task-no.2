#this is simple calculator project that i have created for my internship!!!!
while True:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print("numbers entered are  ", a, "and", b)
    print("operations that can be performed are : \n 1.addition \n 2.subtraction \n 3.multiplication \n 4.division")

    #now im going to ask my user to choose an option or operation that the user wishes to work on with.
    #using match-case for switching  between different operations and note that match case doesnt support tuple datatypes so we need to use " | " for providing multiple options under same case

    choice=input("enter the desired operation to perform : ")
    match(choice):
        case ('1'|'add'|'Add'|'ADD'|'Addition'|'ADDITION'|"+"|"addition"):
            add=a+b
            print("your choice is addition operation \n the sum is : ", add)
        case ("2"|"sub"|"Sub"|"SUB"|"Subtraction"|"SUBTRACTION"|"minus"|"Minus"|"MINUS"|"-"):
            print("your choice is subtraction operation")
            if a>b:
                print("number",a,"is greater than",b)
                sub=a-b
                print("the difference is  : ", sub)
            elif a==b:
                print("the difference is : 0")
            else:
                print("number",b,"is greater than",a)
                sub=b-a
                print("the difference is : ", sub)
        case ("3"|"Multiplication"|"MULTIPLICATION"|"multiply"|"mul"|"MUL"|"Product"|"PRODUCT"|"product"|"*"):
            multiply=a*b
            print("Your choice is Multiplication \n the product is : ",multiply)
        case ("4"|"divide"|"division"|"DIVIDE"|"Division"|"DIVISION"|"Division"|"/"):
            print("your choice is division  operation")
            if b==0:
                print("Error! division by zero is not allowed.")
            else:
                division=a/b
                quoient=a//b
                remainder=a%b
                print("the result is : ",division)
                print("the quoient is : ", quoient)
                print("the remainder is : ",remainder)
    userchoice=input("do you want to continue : (yes /no)")
    if userchoice not in ['yes','Yes', 'YES', 'y', 'Y']:
        print("exiting the code!!!!...thank you...visit again!!!!")
        break


