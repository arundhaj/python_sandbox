# a sample program to learn function

def addition(a, b):
	return a + b

c = int(input('Enter a:'))
d = int(input('Enter b:'))

print('sum of {0} and {1} is {2}'.format(c, d, addition(c, d)))
