import random

#a = [1,1,2,3,5,8,13,21,34,55,89]
#b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

a = []
b = []
c = []
n_a = random.randint(1,20)
n_b = random.randint(1,20)

for x in range(n_a):
	a.append(random.randint(1,30))
for x in range(n_b):
	b.append(random.randint(1,30))

for i in a:
	if (i in b) and (i not in c):
		c.append(i)

for i in b:
	if (i in a) and (i not in c):
		c.append(i)

print(c)