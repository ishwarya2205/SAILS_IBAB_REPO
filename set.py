# create with a set
empty_set=set()
even_numbers={0,2,4,6,8}
print(even_numbers)

# convert from other data types with set()
new_set=set("letters")
print(new_set)

#set from a list
lset=set(["virat","rohit","shubham"])
print(lset)

#test for a value using in-values are set
playerscores={
        "rohit":{53,87,96},
        "virat":{128,21,78},
        "shubham":{23,44,85}
}
for name,scores in playerscores.items():
    if 123 in scores:
        print(name)


    for v in scores:
            if v>=50:
                print(name)
                break


a={1,2}
b={2,3}
print(a&b)
print(a.intersection(b))
print(a.union(b))
print(a-b)
print(a.difference(b))
print(a^b)
print(a.symmetric_difference(b))
print(a<=b)
print(a.issubset(b))
print(a<b)
print(a>=b)









