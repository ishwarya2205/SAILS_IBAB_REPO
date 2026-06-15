# setup python environment and use python shell and command line to execute python programs



# write a program to print "hello world!"
s="hello world"
print(s)


# write a program to convert fahrenheit to celsius. keep the conversion logic in a separate function.
def farenheit_to_celcius(f):
    c = (5/9) * (f - 32)
    return c


def value():
    f = 190
    c = farenheit_to_celcius(f)

    print("c")

if __name__ == "__main__":
    value()



def swap(a, b):
    return b, a

# write a program to swap two numbers. Keep the swap logic in a separate function.
def value():
    a = 8
    b = 5
    newa, newb = swap(a, b)
    print(newa, newb)


if __name__ == "__main__":
    value()





# write a program to check if a given number is odd or even. keep the logic in a separate function.
def check(num):
	if num % 2==0:
	    print("even")
	else:
	    print("odd")



if __name__== "__main__":
    num=int(input("1"))
    check(num)

