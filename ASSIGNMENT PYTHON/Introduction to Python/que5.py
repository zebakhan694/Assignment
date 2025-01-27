# write a program to get factorial number of given number
#    5 = 1*2*3*4*5

num = int(input("Enter a Number : "))
fact=1

for i in range(1,num+1):
    fact*=i

print(fact)
