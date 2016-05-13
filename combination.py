n = input(">>> Input n: ")
r = input(">>> Input r: ")

def mul(x,y):
	return x*y

ans=reduce(mul,range(n-r+1,n+1))/reduce(mul,range(1,r+1))

print "Answer: %d" % (ans)


"""
n_factorial=n
r_factorial=1
ans=0
temp=1

while(temp<=r):
	n_factorial=n_factorial*(n-1)
	n-=1
	r_factorial*=temp
	temp+=1

ans=n_factorial/r_factorial

print "Answer: %d" % (ans)

"""
