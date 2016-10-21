number = input("Give a number: ")

if int(number) % 4 == 0:
	print("It's a multiple of 4!")
elif int(number) % 2 == 1:
	print("This is an odd number")
elif int(number) % 2 == 0:
	print("This is an even number")

num = input("Give a number to check:")
check = input("Give a number to devide:")

if (num != "") and (check != ""):
	num = int(num)
	check = int(check)
	
	if num % check == 0:
		print("Your number is evenly devided by the check number.")
	else:
		print("Your number is not evenly devided by the check number!")
else:
	print("Error, you didn't input anything.")