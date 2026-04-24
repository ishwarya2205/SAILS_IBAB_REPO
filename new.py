def fibinocci():
	a=0
	b=1
	n=10
	for i in range (0,n):
	    sum=a+b
	    print(sum)
	    a=b
	    b=sum
	
def mymain():
    fibinocci()
    
if __name__== "__main__":
	mymain()
