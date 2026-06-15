# write a function that computes power - raise base to the n-th power. Eg. power(2,5). Here base is 2 and n-th power is 5.
# doubt
def power(base, n):
    """
    Computes base raised to the power n.
    Handles negative exponents and fractional bases.
    """
    # Handle negative exponents
    if n < 0:
        base = 1 / base
        n = -n

    result = 1
    current_product = base

    while n > 0:
        # If n is odd, multiply the current product with the result
        if n % 2 == 1:
            result *= current_product
            # Square the base and halve the exponent
            current_product *= current_product
            n //= 2

        return result

    # Example Usage:
print(power(2, 5))  # Output: 32
print(power(3, 4))  # Output: 81
print(power(2, -3))  # Output: 0.125


# write a function to check if a given number, N, is prime or not.
def is_prime(n):
# numbers less than 2 are not prime
    if n < 2:
        return False
	    

    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return False   # found a factor, so it is not prime
    return True # no factors found, it is prime
    
def mymain():
# test the function on numbers from 0 to 9
    for i in range(1,10):
        if is_prime(i):
            print(f"{i} is prime")
        else:
            print(f"{i} is not prime")
    
if __name__== "__main__":
    mymain()


# write a function to print individual digits of a number, N
# Method 1: Mathematical Approach (Most universal across languages)
def print_digits_math(n):
    """Prints digits from left to right using math."""
    if n == 0:
        print(0)
        return

    # Handle negative numbers
    n = abs(n)

    # 1. Reverse the number to easily extract left-to-right digits
    reversed_num = 0
    temp = n
    while temp > 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp //= 10

    # 2. Print digits from the reversed number
    while reversed_num > 0:
        print(reversed_num % 10)
        reversed_num //= 10


# Method 2: String Approach (Simplest and cleanest in Python)
def print_digits_string(n):
    """Prints digits from left to right using string conversion."""
    # Convert absolute value to string to avoid printing negative signs
    for digit in str(abs(n)):
        print(digit)


# Example Usage:
print("--- Math Approach ---")
print_digits_math(4502)

print("--- String Approach ---")
print_digits_string(4502)



