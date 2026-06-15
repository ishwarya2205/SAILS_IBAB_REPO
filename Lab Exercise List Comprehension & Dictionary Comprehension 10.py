# You are given a list called fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'].  Create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...].
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
capitalized_fruits = [fruits.capitalize() for fruits in fruits]
print(capitalized_fruits)

# You are given a list called fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'].Make a variable named fruits_with_only_two_vowels. Use list comprehension to produce ['mango', 'kiwi', 'strawberry'], a list of fruits with only two vowels.
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
vowels = ['a','e','i','o','u']

fruits_with_only_two_vowels = []

# Given org1 = ["ACGTTTCA", "AGGCCTTA", "AAAACCTG"], org2 = ["AGCTTTGA", "GCCGGAAT", "GCTACTGA"],  find all similar pairs of genome sequences (one sequence from org1, one from org2) using list comprehension. “Similar” means: similarity(seq1, seq2) > threshold
# doubt
org1 = ["ACGTTTCA", "AGGCCTTA", "AAAACCTG"]
org2 = ["AGCTTTGA", "GCCGGAAT", "GCTACTGA"]

threshold = 5

def similarity(seq1, seq2):
    count = 0
    for a, b in zip(seq1, seq2):
        if a == b:
            count += 1
    return count

similar_pairs = [
    (s1, s2)
    for s1 in org1
    for s2 in org2
    if similarity(s1, s2) > threshold
]

print(similar_pairs)

# Given numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Create a dictionary of numbers and their squares, excluding odd numbers using dictionary comprehension
# doubt
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = {num: num**2 for num in numbers if num % 2 == 0}

print(squares)

# sentence = "Hello, how are you?". Write a dictionary comprehension to map words to their reverse in a sentence. The output should be - {'Hello,': ',olleH', 'how': 'woh', 'are': 'era', 'you?': '?uoy'}
# doubt
sentence = "Hello, how are you?"

result = {word: word[::-1] for word in sentence.split()}

print(result)



