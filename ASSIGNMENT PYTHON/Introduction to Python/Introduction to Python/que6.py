# Write a Python program to get the Fibonacci series of given range. 

def fibonacci_in_range(start,end):
    fib_series = []
    a,b = 0,1
    while a<=end:
        if a>=start:
            fib_series.append(a)
        a,b = b, a+b
    return fib_series        


start_range = int(input("Enter the start of the range : "))
end_range = int(input("Enter the end of the range : "))


result = fibonacci_in_range(start_range,end_range)
print(f"fibonnaci series in range [{start_range},{end_range}]:")
print(result)