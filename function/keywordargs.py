# a sample to learn function arguments passing with keyword

def volume(l, b, h):
	return l * b * h

print 'volume of object 1 is:',volume(l = 2, b = 3, h = 4)
print 'volume of object 2 is:',volume(h = 4, l = 2, b = 3)
