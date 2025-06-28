#  How many except statements can a try-except block have? Name Some built-in exception classes:

"""
   A try-except block can have multiple except statements, each handling a specific exception.
"""

try: 
    num1 = int(input("Enter first Number : "))
    num2 = int(input("Enter second Number : "))
    ans = num1/num2
    print(ans)

except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("Invalid input..!! please enter a number")

except Exception as e:
    print(f"An unexpected error occured : {e} ")


# SOME BUILT IN EXCEPTION CLASSES IN PYTHON

"""
1) zeroDivisionError :- raised when a number is divided by zero
2) valueError :-  raised when function recieves a invailid argument
3) TypeError :- raised when a operation is performed on incompatible types
4) IndexError :- raised when accessing an invalid index in a list
5) KeyError :- raised when a dictionary key is not found
6) NameError :- raised when accessing a undefined variable
7) FileNotfoundError :- raised when file is not found
8) AttributeError :- raised when invalid attribute refrence is made 
"""
