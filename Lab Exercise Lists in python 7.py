# setup pycharm, virtual environments and github repositories


# write a function to find the sum and average of numbers in a list,L
def calculate_stats(l):
	if not l:
		return 0,0
	total_sum=sum(l)
	average=total_sum/len(l)
	return total_sum,average

mu_list=[10,20,30,40,50]
s,a=calculate_stats(mu_list)


# write a function to find the minimum and maximum number in a list, L
numbers=[1,2,3,4,5,6,9,8]
numbers=[5,9,1,6,8,9]
def minimum_maximum(numbers):
    for i in numbers:
        n=sorted(numbers)
        minimum=n[0]
        maximum=n[len(numbers)-1]
    print(minimum,maximum)

x = minimum_maximum(numbers)

# not mine
def find_min_max_builtin(L):
	# Handle an empty list case safely
	if not L:
		return None, None

	minimum = min(L)
	maximum = max(L)

	return minimum, maximum
# Example usage:
numbers = [23, 5, 87, 1, 42]
lowest, highest = find_min_max_builtin(numbers)
print(f"Minimum: {lowest}, Maximum: {highest}")  # Output: Minimum: 1, Maxim

# write a program to find the even numbers in a list,L
l=(2,3,4,5,6,7,8,9,10)
def even_numbers(l):
    for i in l:
        if i%2==0:even_numbers()
        else: even_numbers()
        print(even_numbers)

l=(2,3,4,5,6,7,8,9,10)

# write a program to print the duplicate elements in a list, L
l = [1,2,3,4,5,6,7,8,9,10,1,2,3]

seen = set()
duplicate = set()

for item in l:
	if item in seen:
		duplicate.add(item)
	else:
		seen.add(item)

print(duplicate)

# write a program to subtract two matrices, m1 and m2, using a list of lists
def matrix_substraction():
# define the matrix

	m1 = [[5, 8, 3],
      	  [6,7, 9]]

	m2 = [[1, 2, 1],
          [4, 2, 3]
	]

# give an empty list to finally store the result rows
	result = []

# row to column substraction
	val1 = (m1[0][0] - m2[0][0])
	val2 = (m1[0][1] - m2[0][1])
	val3 = (m1[0][2] - m2[0][2])
	result.append([val1, val2, val3])


	val4 = (m1[1][0] - m2[1][0])
	val5 = (m1[1][1] - m2[1][1])
	val6 = (m1[1][2] - m2[1][2])
# use append to store the values as matrix
	result.append([val4, val5, val6])

	print(result)


matrix_substraction()

# write a program to extract elements of a list, if it occurs more than k times.
# i have doubt in this
fruits = ("apple", "orange", "guava", "cherry", "apple")
k = 1

result = []
for item in fruits:
	if fruits.count(item) > k and item not in result:
		result.append(item)

	print(result)


# write a program to remove all occurences of an element from a list, L
l = [1, 2, 3, 4, 5, 2, 2, 2]
target = 2

total_appearances = l.count(target)

for i in range(total_appearances):
	l.remove(target)
print("updated list", l)


# write a program to extract words from a string list, L whose first character is k

l = ["mango", "apple", "orange", "cherry", "guava", "mango", "mango", "coconut"]
k = "m"

extracted_words = []

for word in l:
	if word[0] == k:
		extracted_words.append(word)
print(extracted_words)















