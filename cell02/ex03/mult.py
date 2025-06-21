num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
n = num1*num2
if n > 0:
    print("The result is positive")
    print(num1,"x",num2,"=",n)
if n < 0:
    print("The result is negative")
    print(num1,"x",num2,"=",n)
if n ==0:
    print("The result is both positive and negative") 
    print(num1,"x",num2,"=",n) 
