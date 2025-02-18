#  When is the finally block executed?

"""
   The finally block always executed, no matter exception occur in try block or not.
   it is mainly used for clean up operations, like closing files, closing database connections or releasing resources etc.
"""

try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    ans = num1/num2
    print(ans)

except(ZeroDivisionError,ValueError,TypeError) as e:
    print(f"Error occured : {e}")

finally:
    print("This is always executed")