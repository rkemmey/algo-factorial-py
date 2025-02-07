def factorial(num):
	# your code here
	if num < 0:
		return "Num must be positive"
	if not isinstance(num, int):
		return "Num must be an integer"
	if num == 0:
		return 1
	else:
		product = 1
		for i in range(num, 1, -1):
			#print(i)
			product = product * i
		return product
		

