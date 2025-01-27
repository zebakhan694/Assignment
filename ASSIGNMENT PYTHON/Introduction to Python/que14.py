# Write a Python program to sum of the first n positive integers.

n=int(input("Enter how many elements you want to enter : "))
sum=0 

for num in range(1,n+1):
    num=int(input("Enter a number : "))
    if num%2==0:
        sum+=num
print(f"sum of integer values is {sum}")

