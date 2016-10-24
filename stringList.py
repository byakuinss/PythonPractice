sen = input("Give a string: ")

flag = False
end = len(sen)-1
mid = len(sen)/2
mid = int(mid)

for i in range(0,mid):
	if(sen[i] == sen[end-i]):
		flag = True
	else:
		flag = False

if(flag == True):
	print(sen + " is a palindrome.")
else:
	print(sen + " is not a palindrome.")