#  Write a Python function to check whether a number is perfect or not.
"""
6 --> proper diviser: 1,2,3   --> 1 + 2 + 3 = 6
"""
def is_perfect_number(n):
    if n <=0:
        return False
    
    sum_of_divisors = 0
    for i in range(1,n):
        if n%i==0:
            sum_of_divisors+=i

    return sum_of_divisors == n

num = int(input("Enter a Number: "))
if is_perfect_number(num):
    print(f"{num} is a perfect nhumber.")
else:
    print(f"{num} is not a perfect nhumber.")

      