print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10 12 15 "))

people = int(input("How many people to split the bill? "))

each_person=(bill*(1+(tip/100)))/people
each_person=round(each_person,2)


print("Each person should pay: "+ str(each_person))
print(f"Each person should pay:$100{each_person}")

