#  Write python program that user to enter only odd numbers, else will raise an exception.

def get_odd_number():
    try:
        number = int(input("Enter an odd number: "))
        if number % 2 == 0:
            raise ValueError("That's not an odd number!")
        print(f"Thank you! You entered an odd number: {number}")
    except ValueError as e:
        print(f"Error: {e}")

# Run the function
get_odd_number()

