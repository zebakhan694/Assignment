# Write a program to check if a person is eligible to donate blood using nested if.

"""
Eligiblity Criteria : 
                        1) Age = 18-65
                        2) Weight = more than 50kg
                        3) Hemoglobin Level = 12.5 g/dL
"""

age = int(input("Enter Your Age : "))

if age>=18 and age<=65:
    weight = int(input("Enter Your Weight : "))
    
    if weight>=50:
        hemoglobin = int(input("Enter Your Hemoglobin Level : "))
        
        if hemoglobin>=12.5:
            print("You are Eligible to donate blood")
        else:
       
            print("Your Hemoglobin Level is Low")
    else: 
        print("You are under Weight")   

else:
    print("You are not eligible to donate blood due to your age")