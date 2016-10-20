import datetime

name = input("What's your name: ")
age = int(input("What's your age: "))
this_year = int(datetime.datetime.now().year)

print("You will be 100 years old at: " 
	+ str(100 - age + this_year))

