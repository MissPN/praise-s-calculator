print("enter operation")

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divivide")

operation = input()
if operation == "1":
    num1 = input("enter first number ")
    num2 = input("enter second number ")
    print("the sum is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("enter first number")
    num2 = input("enter second code")
    print("the difference is " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("enter first number")
    num2 = input("enter second number")
    print("the product is " + str(int(num1) * int(num2)))
elif  operation == "4":
    num1 = input("enter first number")
    num2 = input("enter second number")
    print("the reuslt is " + str(int(num1) / int(num2)))
else:
    print("invalid option ")