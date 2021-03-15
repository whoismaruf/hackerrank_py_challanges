def loops(n):
	if n in range(1,20):
		for i in range(0, n):
			print(i**2)
	else:
		print("Please input a number beetween 1 to 20")


if __name__ == '__main__':
	n_int = 3
	loops(n_int)