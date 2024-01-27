height = float(input("Enter height in meters as a floating point number e.g: 1.65:\n"))
weight = int(input("Enter weight in kilograms as an integer e.g: 72:\n"))
# Your code below this line 👇
bmi = weight / (height * height)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")