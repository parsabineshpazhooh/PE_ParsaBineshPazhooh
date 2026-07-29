# Simple calculator
number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))
operator = input("What do you wanna do? ")
if operator == "+":
    print(int(number_1 + number_2))
elif operator == "-":
    print(int(number_1 - number_2))
elif operator == "*":
    print(int(number_1 * number_2))
elif operator == "/":
    print(int(number_1 / number_2))
print("authed by \n* P.BineshPazhooh *")