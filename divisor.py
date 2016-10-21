num = input("Please input a number:")
num = int(num)

x = range(2, num)
b = []

for i in x:
	if num % i == 0:
		b.append(i)

print(b)