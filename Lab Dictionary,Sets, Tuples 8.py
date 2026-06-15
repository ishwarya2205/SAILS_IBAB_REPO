# write a program to iterate over a dictionary and print key and values
from sklearn.externals.array_api_compat.dask.array import unique_values
lifecycle = {
    "happiness": 100,
    "satisfactory": 200,
    "sorrow": 1,
    "friendship": 80
}
for key, value in lifecycle.items():
    print(key, value)

# write a program to sum all values of a dictionary
lifecycle = {
    "happiness": 100,
    "satisfactory": 200,
    "sorrow": 1,
    "friendship": 80
}
for total in lifecycle:
    total_values = (sum(lifecycle.values()))
    print(total_values)

# write a program to find the maximum and minimum value of a dictionary
lifecycle_scores = {
    "happiness": 100,
    "satisfactory": 200,
    "sorrow": 1,
    "friendship": 80
}
scores = lifecycle_scores.values()
highest = max(scores)
lowest = min(scores)
print(highest)
print(lowest)

# given a dictionary with a values list, extract the key whose value has the most unique values.
    #Input : test_dict = {"Gfg" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
    #Output : "Best"
    #Explanation : 3 (max) unique elements, 9, 6, 5 of "Best".
test_dict = {
    "gfg": [5, 7, 7, 7, 7],
    "is": [6, 7, 7, 7],
    "best": [9, 9, 6, 5, 5]
}
unique_counts = {}

for key, values_list in test_dict.items():
    unique_counts[key] = len(set(values_list))

maximum = max(unique_counts.values())

for key, count in unique_counts.items():
    if count == maximum:
        print(key)

# Remove all duplicate words from given sentence using a dictionary
sentence_n="india is a good country, india is a fastest growing economy in the world, india is a world largest democracy, all my indians are brothers and sisters, i love india because i'm indian"

split_words= sentence_n.split()
unique_dict= dict.fromkeys(split_words)
clean_sentence = " ".join(unique_dict)
print(unique_dict)
print(clean_sentence)

# The common friends finder: you have two sets of user IDs: followers and following.
# a. write a program to find "mutuals" (people who follow you AND you follow back)
# b. Find "fans" (people who follow you, but you don't follow back)
# doubt
followers = {1, 2, 3, 4, 5}
following = {3, 4, 5, 6, 7}

mutuals = followers & following
fans = followers - following

print("Mutuals:", mutuals)
print("Fans:", fans)