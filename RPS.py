
play = input("Do you want to play?(y/n)")

user_a = input("Player_A: ")
user_b = input("Player_B: ")

while play == 'y':
	a_answer = input("Player_A please choose rock, scissors or paper (r/s/p): ")
	b_answer = input("Player_B please choose rock, scissors or paper (r/s/p): ")

	if a_answer == 'r':
		if b_answer == 's':
			print("%s win!" % user_a)
		elif b_answer == 'p':
			print("%s win!" % user_b)
		else:
			print("No one win.")
	elif a_answer == 'p':
		if b_answer == 'r':
			print("%s win!" % user_a)
		elif b_answer == 's':
			print("%s win!" % user_b)
		else:
			print("No one win.")
	elif a_answer == 's':
		if b_answer == 'p':
			print("%s win!" % user_a)
		elif b_answer == 'r':
			print("%s win!" % user_b)
		else:
			print("No one win.")
	else:
		print("No one win.")
	play = input("Do you want to play again?(y/n)")

print("The end.")
