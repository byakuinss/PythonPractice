a = [1,1,2,3,5,8,13,21,34,55,89]
num = input("Please input a number: ")

b = []

for i in a:
	if i < int(num):
		#print(i)
		b.append(i)

print(b)

