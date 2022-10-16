weight = float(0.453592)
height = float(0.0254)


Weight_input = float(input("How much do you weigh?"))
Height_input = float(input("How tall are you?"))


#print(f"Your weight is  {Weight_input * weight}")
#print(f"Your height is {Height_input * height}")

numberw = float(Weight_input * weight)
numberh = float(Height_input * height)




bmi = (numberw / numberh**2)

tbmi = bmi
print(tbmi)






