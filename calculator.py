def calculator(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("The Operator is not valid!!!")
        

    print(result)


try:
    num1 = int(input("Please Enter Number 1 : "))
    operator = input("Please Enter The Operator [ *, +, - , / ] : ")
    num2 = int(input("Please Enter Number 2 : "))
except:
    print("Opss! Something Went Wrong!!!")

else:
    calculator(num1, operator, num2)
    








