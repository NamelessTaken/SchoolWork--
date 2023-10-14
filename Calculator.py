print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
oper = int(input("""Enter a number between 1-6:
                 press 1 for addition
                 press 2 for subtraction
                 press 3 for multiplication
                 press 4 for division
                 press 5 to find square of a number
                 press 6 to find square root of a number
                 :: """))
if oper == 1:
    print("the sum of the numbers is",(a+b))
elif oper == 2:
    print("the difference between the two numbers is",(a-b))
elif oper == 3:
    print("the product of the two numbers is",(a*b))
elif oper == 4:
    print("the value for",a,"/",b,"is",(a/b))
elif oper == 5:
    c = input("Would you like to use existing numbers or use new numbers to square(y/n):: ")
    if c == 'y':
        d = input("""Select a number between your given number:
                  press 'a' to find square of your first number
                  press 'b' to find square of the second number
                  :: """)
        if d == 'a':
            print("the square of the number",a,"is",(a**2))
        elif d == 'b':
            print("the square of the number",b,"is",(b**2))
        else:
            print("Invalid Input")
    elif c == 'n':
        e = int(input("Enter a new number to find the square of:: "))
        print("the square of the number",e,"is",(e**2))
elif oper == 6:
    f = input("Would you like to use existing numbers or use new numbers (y/n):: ")
    if f == 'y':
        g = input("""Select a number between your given number:
                  press 'a' to find square root of your first number
                  press 'b' to find square root of the second number
                  :: """)
        if g == 'a':
            print("the square root of the number",a,"is",(a**0.5))
        elif g == 'b':
            print("the square root of the number",b,"is",(b**0.5))
        else:
            print("Invalid Input")
    elif f == 'n':
        h = int(input("Enter a new number to find the square root of:: "))
        print("the square root of the number",h,"is",(h**2))
else:
    print("Invalid Input")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
