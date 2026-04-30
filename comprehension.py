number_list=list(range(1,6))
print(number_list)


number_list=[number for number in range(1,6)]
print(number_list)
number_list=[number -1 for number in range(1,6)]
print(number_list)
a_list=[number for number in range(1,6) if number % 2==1]
print(a_list)
b_list=[number for number in range(1,6) if number % 2==0]
print(b_list)

rows=range(1,4)
cols=range(1,3)
for row  in rows:
    for col in cols:
        print(row,col)


rows=range(3,4)
cols=range(1,3)
cells=[(row,col) for row in rows for col in cols]
for cell in cells:
    print(cell)
for row, col in cells:
    print(row,col)


# dictionary comprehension
# {key_expression: value_expressions for expression in iterable)
word='letters'
letter_counts={letter:word.count(letter) for letter in word}
print(letter_counts)





