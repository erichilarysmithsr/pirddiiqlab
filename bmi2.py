#YellowFit CORE BMI Calculator
#Get Patient Weight in pounds and Patient Height in Inches
patientWeight = float(input('Please enter your weight in (lbs):  '))
patientHeight = float(input('Please enter your height in (inches):  '))
#Calculate Patient BMI Score
h = (patientHeight * patientHeight)
w = patientWeight
BMI = (w / h) * 703

if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")