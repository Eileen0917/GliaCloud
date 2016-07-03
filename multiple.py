multiple=[]
sum=0
a=0
b=0
c=0

while(a<=1000):
	if(a%3==0 or a%5==0):
		multiple.append(a)
		a+=1
	else:
		a+=1

for i in range(0,len(multiple)-1):
	sum+=multiple[i]

print "Answer: %d" % (sum)