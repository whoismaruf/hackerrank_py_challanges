def checking(n):
	if n%2 == 0:
		if (n in range(2,5)) or n>20:
			if n in range(6,20):
				print("weird")
			else:
				print("Not weird")
		else:
			print("weird")
	else:
		if n%2 != 0:
			print("weird")
		else:
			print("Invalid")


x = input("Enter number: ")
checking(int(x))