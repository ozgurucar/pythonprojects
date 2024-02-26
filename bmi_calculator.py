height = int(input("Enter your height as centimeter"))
weight = int(input("Enter your weight as kilogram"))
height_in_meters = height / 100
bmi = weight / (height_in_meters * height_in_meters)
bmi = round(bmi, 2)
print(f"Your bmi is {bmi}")
if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi < 25:
    print("You are in healthy range")
elif 25 <= bmi < 30:
    print("You are overweight")
elif 30 <= bmi < 40:
    print("You are obese")
elif bmi >= 40:
    print("You are in severe obesity section")
