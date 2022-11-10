#YellowFit CORE BMI Calculator
#Get Patient Weight in pounds and Patient Height in Inches
patientWeight = float(input('Please enter your weight in (lbs):  '))
patientHeight = float(input('Please enter your height in (inches):  '))
#Calculate Patient BMI Score
h = (patientHeight * patientHeight)
w = patientWeight
BMI = (w / h) * 703

if BMI <= 18.4:
    print("You most likely need to eat more to gain weight in a normal range.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You most likely need to lose weight and exercise more to reduce the further risk of obesity.")
elif BMI <= 34.9:
    print("You need to report to local health care provider for nutrition consultation for specific diets and weight loss programs in your community.")
elif BMI <= 39.9:
    print("You may have to be tested or retested for Type 2 Diabetes from your local health care provider in your community.")
else:
    print("You are severely obese.")