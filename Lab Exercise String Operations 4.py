# print half of the string
s="python language"
first_half=(s[2])
print(first_half)

# print alternate characters of a string
def skip_characters(text):
	return text[::2]

def mymain():
	s = "india pakistan"
	result = skip_characters(s)
	print(result)

if __name__ == "__main__":
    mymain()


# write a program to concatenate of a string

def concatenate_string(l1, l2):
	return l1+l2

words = ["india", "is", "a", "beautiful", "country"]
print(concatenate_string(words, words))

# find first occurence of a character in a string

def find_first_char_loop(text, target):
	# loop through the string tracking the index 'i'
	for i in range(len(text)):
		if text[i] == target:
			return i # return the index immediately when found
	return -1

print(find_first_char_loop("india is a beautiful country", "i"))


# find highest frequency character in a string
def highest_freq_char(text):
	if not text:
		return None

	# Step 1: Count frequencies of each character
	char_counts = {}
	for char in text:
		char_counts[char] = char_counts.get(char, 0) + 1

	# Step 2: Find the character with the maximum count
	max_char = text[0]
	max_count = 0

	for char, count in char_counts.items():
		if count > max_count:
			max_count = count
			max_char = char

	return max_char
print(highest_freq_char("india is a beautiful country"))


# Replace all occurences of a character with another character

s="india pakistan"
new_text=s.replace("z","@")
print(new_text)
# this is negative side



s="india pakistan"
new_text=s.replace("a","@")
print(new_text)
# this is positive side

# Trim leading whitespace characters from a string

def trim_leading_builtin(text):
    # Removes all whitespace characters from the left side
    return text.lstrip()

# Example usage:
sample_text = "   Hello World   "
result = trim_leading_builtin(sample_text)

print(f"Original: '{sample_text}'")
print(f"Trimmed:  '{result}'")
# Output: 'Hello World   ' (Notice the spaces at the end remain)


# count no of occurences of a word in a sentence

s="india is a largest economy and india is a good country"
word_list=s.lower().split()
result=word_list.count("india")
print(result)
