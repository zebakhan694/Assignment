#  Can one block of except statements handle multiple exception?

"""
   yes! A single except block can handle multiple exceptions by using a tuple.
   it helps the code clean and avoids repetitive except statements.
"""

try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    ans = num1/num2
    print(ans)

except(ZeroDivisionError,ValueError,TypeError) as e:
    print(f"Error occured : {e}")
