# check if two strings are anagrams of each other - use sort function - listen and silent are anagrams, gram and arm are not anagrams.
# doubt
def are_anagrams(str1, str2):
    """
    Checks if two strings are anagrams by sorting their characters.
    """
    # Remove whitespace and convert to lowercase for fair comparison
    clean_str1 = str1.replace(" ", "").lower()
    clean_str2 = str2.replace(" ", "").lower()

    # Sort both strings and compare
    return sorted(clean_str1) == sorted(clean_str2)


# Testing the examples
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("gram", "arm"))  # Output: False

# check if a given string is palindrome or not
word = "ishwarya"

def is_palindrome():
    if word[:] == word[::-1]:
        print(word + "is a palindrome")

    else:
        print(word + "is not a palindrome")

def mymain():
    is_palindrome()

if __name__ == "__main__":
    mymain()

# positive palindrome
word = "madam"

def is_palindrome():
    if word[:] == word[::-1]:
        print(word + "is a palindrome")

    else:
        print(word + "is not a palindrome")

def mymain():
    is_palindrome()

if __name__ == "__main__":
    mymain()

# print all k-mers of a given string
# The input DNA sequence
kmer_string = "ATGCAATGCAATGCA"

def get_kmers(sequence, k=4):
    """Extracts and prints all overlapping k-mers of size k."""
    # Loop from 0 up to the last index where a valid k-mer can start
    for i in range(len(sequence) - k + 1):
        # Slice the string from index i to i + k
        kmer = sequence[i:i + k]
        print(kmer)

def mymain():
    # Call the function with our string
    print(f"--- 4-mers for {kmer_string} ---")
    get_kmers(kmer_string, k=4)

if __name__ == "__main__":
    mymain()

# implement a method to perform basic string compression using the counts of repeated characters (Eg., aabcccccaaa becomes a2b1c5a3)
# doubt
def compress_string(text):
    """
    Compresses a string using the counts of repeated characters.
    Returns the original string if the compressed version isn't shorter.
    """
    # Quick exit for empty or single-character strings
    if not text:
        return text

    compressed = []
    count = 1

    # Iterate through the string starting from the second character
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            # Append the previous character and its count
            compressed.append(text[i - 1] + str(count))
            count = 1  # Reset count for the new character

    # Append the last character group after the loop finishes
    compressed.append(text[-1] + str(count))

    # Join the list into a single string
    compressed_str = "".join(compressed)

    # Return the original string if compression didn't save space
    return compressed_str if len(compressed_str) < len(text) else text

# Example Usage:
print(compress_string("aabcccccaaa"))  # Output: a2b1c5a3
print(compress_string("abcd"))         # Output: abcd (a1b1c1d1 is longer)








