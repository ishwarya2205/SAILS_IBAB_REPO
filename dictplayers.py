dictplayers={
    "rohit":78,
    "gill":80,
    "kohli":45
}
dictplayers["ishan"]=90
dictplayers["gill"]=125
dictplayers["gill"]=130
print(dictplayers)


# delete an item key with del
del dictplayers["siraj"]
temp=dictplayers.copy()
dictplayers.clear()
dictplayers=temp.copy()
print(dictplayers)


# test or a key by using in

print("rohit" in dictplayers)
print(dictplayers)


# get an item by [key]
print("gill" in dictplayers)


#get an item
print(dictplayers["gill"])


#get all keys
k=dictplayers.keys()
print(type(k))
print(dictplayers.keys())
print(list(dictplayers.keys())
d=list(dictplayers.key())
print(type(d))
print(list(dictplayers.keys()))


#get all values
print(list(dictplayers.values()))


#get all key value pairs using items
print(list(dictplayers.items()))
print(dictplayers.get("shyam"))
