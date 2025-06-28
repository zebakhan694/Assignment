# How Do You Handle Exceptions with Try/Except/Finally in Python? Explain with coding snippets.

try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    ans = num1/num2
    
except(ZeroDivisionError,ValueError,TypeError) as e:
    print(f"Error occured : {e}")

else:
    print(ans)
    
finally:
    print("This is always executed")