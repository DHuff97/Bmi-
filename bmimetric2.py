#weight = float(0.453592)
#height = float(0.0254)


Weight_input = float(input("Please enter weight in kilograms: "))
Height_input = float(input("Please enter height in meters: "))


#print(f"Your weight is  {Weight_input * weight}")
#print(f"Your height is {Height_input * height}")

#numberw = float(Weight_input * weight)
#numberh = float(Height_input * height)




bmi = (Weight_input / Height_input**2)

tbmi = round(bmi, 2)
if tbmi <= 18.5:
    print(f"bmi is: {tbmi}, status is underweight")
elif tbmi <= 24.9:
    print(f"bmi is: {tbmi}, Status is normal")
elif tbmi <= 29.9:
    print(f"bmi is: {tbmi}, You are overweight")
else:
    print("obese")






