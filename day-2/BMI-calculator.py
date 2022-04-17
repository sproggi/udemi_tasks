# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = int(weight / height**2)
if bmi <= 18:
  print(f'Your BMI is {bmi}, you are underweight.')
elif 18 < bmi <= 22:
  print(f'Your BMI is {bmi}, you are a normal weight.')
elif 22 < bmi <= 28:
  print(f'Your BMI is {bmi}, you are slightly overweight.')
elif 28 < bmi <= 33:
  print(f'Your BMI is {bmi}, you are obese.')
else:
  print(f'Your BMI is {bmi}, you are clinically obese.')
