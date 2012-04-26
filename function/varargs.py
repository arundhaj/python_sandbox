# sample program to learn variable number of arguments

def total(initial=5, *numbers, **keywords):
	count = initial

	for num in numbers:
		count += num
	
	for key in keywords:
		count += keywords[key]
	
	return count

print(total(10, 1, 2, 3, vegetable=50, fruits=100))
