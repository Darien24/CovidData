print("Welcome to my calculator Program")
print("Enter your name:")
name = input()
print("Hello, " + name)


def Addition(num1, num2):
    return num1 + num2

def Subtraction(num1, num2):
    return num1 - num2

def Multiplication(num1, num2):
    return num1 * num2

def Division(num1, num2):
    return num1 / num2

while True:
    select = int(input("Please select operation - \n" \
            "1. Add\n" \
            "2. Subtract\n" \
            "3. Multiply\n" \
            "4. Divide\n"))

    num1 = int(float(input("Please enter the first number: ")))

    num2 = int(float(input("Please enter the second number: ")))


    if select == 1:
        print(num1, "+", num2,  "=",  Addition(num1,num2))

    elif select == 2:
        print(num1, "-", num2, "=", Subtraction(num1,num2))

    elif select == 3:
        print(num1, "*", num2, "=", Multiplication(num1,num2))

    elif select == 4:
        print(num1, "/", num2, "=", Division(num1,num2))

        next_Calculation = input("Would you like to try another calculation?")
        if next_Calculation == "no" or next_Calculation == "No" :
            print("Thanks for Calculating", name)
            break

    else:
        print("Please choose the correct operators, Thank You")
