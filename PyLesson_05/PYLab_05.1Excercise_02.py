height = float(" What is your height: ")
weight = float(" What is your weight: ")
BMI = 0
condition = "Not found" 
def calcInput(BMI):
    return weight/(height*height)*703

if BMI < 18.5:
    condition = "condition is underweight"
elif BMI < 24.9:
    condition = "is normal"
elif BMI < 29.9:
    condition = "overweight" 
elif BMI < 34.9:
    condition = "obese"
elif BMI < 39.9:
    condition = "very obese"
else BMI > 39.9:
    condition = "morbidly obese"

print("Your BMI is", BMI)
print("You are", condition) 



