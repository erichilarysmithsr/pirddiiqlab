#YellowFit CORE BMI Calculator
#Get Patient Weight in pounds and Patient Height in Inches
patientWeight = float(input('Please enter your weight in (lbs):  '))
patientHeight = float(input('Please enter your height in (inches):  '))
#Calculate Patient BMI Score
h = (patientHeight * patientHeight)
w = patientWeight
BMI = (w / h) * 703
# Show Patient Body Mass Index Score(BMI)
print('Your Body Mass Index (BMI) is: ', BMI)


