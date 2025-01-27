# write a python program to sum of three given integers. However, if two values are equal sum will be zero

num1 = int(input("Enter First Number : ")) 
num2 = int(input("Enter Second Number : ")) 
num3 = int(input("Enter Third Number : ")) 


if num1==num2 or num2==num3 or num3==num1:
    sum =0
else:
    sum = num1 + num2 + num3

print(f"sum is {sum}")