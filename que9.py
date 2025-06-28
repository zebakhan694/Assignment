# vWrite python program that swap two number with temp variable and without temp variable.

# swap the numbers by using temp variable
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter First Number : "))

print(f"Befor swapping: First number is {num1} amd Second number is {num2}")
temp = num1        
num1 = num2
num2 = temp

print(f"After swapping: First number is {num1} amd Second number is {num2}")


# swap the number without using temp variable
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

print(f"befor swpping: First number is {a} and Second number is  {b}")

a,b = b,a

print(f"after swpping: First number is {a} and Second number is  {b}")

