Num_of_Peoples = int(input("Enter Number Of People; "))
Cos_of_meal = int(input("Enter Cost Of Each Meal; "))
tax_percentage =eval(input("Enter Sales Tax Percentage; "))
tip_percent = eval(input("Enter Tip Percentage; "))
print("Total Cost Of Food is ",(Num_of_Peoples*Cos_of_meal))
print("Total Sales Tax is ", tax_percentage/100*Num_of_Peoples*Cos_of_meal)
print("Total Tip Amount is ", tip_percent/100*Num_of_Peoples*Cos_of_meal)
print("Total Bill Amount Per Person is ", Num_of_Peoples*Cos_of_meal/Num_of_Peoples) 