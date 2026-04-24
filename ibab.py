def farenheit_to_celcius(f):
	c=((9/5)*(f-32))
	return c
	
def value():
	f=190
	c=farenheit_to_celcius(f)
	
	print(c)
if __name__ =="__main__":
	value()

