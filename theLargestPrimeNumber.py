x=long(600851475143)
a=2



# find prime factor
while(a<x):
	if (x%a==0):
		x=x/a
		a=2
	else:
		a+=1
print "Answer: %d" % (a)


"""

# 1 find factor

factor=[]

while(a<x):
	if (x%a==0):
		factor.append(a)
		a+=1
	else:
		a+=1

# 2 find largest factor that is prime number


print "Answer: %d" % (a)

"""