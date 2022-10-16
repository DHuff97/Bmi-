weight = float(0.453592)
height = float(0.0254)


Weight_input = float(input("Please enter weight in pounds: "))
Height_input = float(input("Please enter height in inches: "))


#print(f"Your weight is  {Weight_input * weight}")
#print(f"Your height is {Height_input * height}")

numberw = float(Weight_input * weight)
numberh = float(Height_input * height)




bmi = (numberw / numberh**2)

tbmi = bmi
print(f"bmi is: {tbmi}")






