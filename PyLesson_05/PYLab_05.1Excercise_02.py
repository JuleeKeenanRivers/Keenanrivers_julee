h = float(input(" What is your height: "))
w = float(input(" What is your weight: "))
bmi = 0

condition = "Not found"
def calcBmi():
    global condition, bmi
    bmi = (703*(w/(h**2)))

    if bmi < 18.5:
        condition = "condition is underweight"
        
    elif bmi < 24.9:
        condition = "is normal"
        
    elif bmi < 29.9:
        condition = "overweight"

        
    elif bmi < 34.9:
        condition = "obese"
        
    elif bmi < 39.9:
        condition = "very obese"
        
    else:
        condition = "morbidly obese"

calcBmi()

print("Your BMI is", bmi)
print("You are", condition) 






  

