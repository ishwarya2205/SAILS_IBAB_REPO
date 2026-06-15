# write a program to print the sum of N integers
numbers=(1,2,3,4,5)
total=sum(numbers)
print(total)



# write a program to print N fibonacci numbers
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




# Fibinocci
def fibinocci():
	a = 0
	b = 1
	n = 0
	while (n <= 10):
		sum = a + b
		print(sum)
		a = b
		b = sum
		n = n + 1


def mymain():
	fibinocci()


if __name__ == "__main__":
	mymain()



# write a program to compute the sum of squares of first N numbers
n=5
sum_of_squares = (n*(n+1)*(2*n+1))/6
print(sum_of_squares)






# write a program to convert the decimal number D into binary
def decimal_to_binary(num):
	return bin(num)[2:]
print(decimal_to_binary)

# write a function that computes the number of 1s in a binary representation of a decimal number, N
# doubt
def count_ones(n):
    """
    Computes the number of 1s in the binary representation of N
    using Brian Kernighan's Algorithm.
    """
    count = 0
    while n > 0:
        n = n & (n - 1)  # Clears the lowest set bit (rightmost 1)
        count += 1       # Increment the 1s counter
    return count

# Example Usage:
# 13 in binary is 1101, which contains three 1s.
print(count_ones(13))  # Output: 3

# write a program to convert the binary number B into decimal
# doubt
# Method 1: Using Python's built-in int() function
def binary_to_decimal_builtin(binary_str):
    """Converts a binary string to decimal using base 2."""
    return int(binary_str, 2)


# Method 2: Manual calculation (Mathematical Approach)
def binary_to_decimal_manual(binary_str):
    """Converts binary to decimal by summing powers of 2."""
    decimal_value = 0
    for digit in binary_str:
        # Shift existing value left (multiply by 2) and add the new bit
        decimal_value = (decimal_value * 2) + int(digit)
    return decimal_value


# Example Usage:
binary_num = "1101"  # 13 in decimal

print(binary_to_decimal_builtin(binary_num))  # Output: 13
print(binary_to_decimal_manual(binary_num))   # Output: 13
