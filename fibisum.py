def fibinocci():
	a=0
	b=1
	n=0
	while (n<=10):
	    sum=a+b
	    print(sum)
	    a=b
	    b=sum
	    n=n+1
	    
def mymain():
    fibinocci()
    
if __name__== "__main__":
	mymain()
