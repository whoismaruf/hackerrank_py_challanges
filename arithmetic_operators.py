def arith_op(a, b):
	if (a in range(1,10**10)) and (b in range(1,10**10)):
		print(a+b)
		print(a-b)
		print(a*b)
	else:
		print("Please input valid number through 1 to 10**10")

arith_op(5,6)