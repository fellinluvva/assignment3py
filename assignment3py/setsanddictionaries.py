print("#1 set creation")
u_set = set()  # empty set
print("Type 'q' to quit")  # to exit the program
while True:
    s_input = input("Enter a number: ")  # input
    if s_input.lower() == 'q':  # break to exit
        break
    try:
        number = int(s_input)
        u_set.add(number)  # if input is number add it to set
    except ValueError:
        print("Invalid input")  # anything except numbers is invalid input
print("Unique set:", u_set)  # return unique set
print("***************")


print("#2 set operations")
set1 = {1, 2, 3, 4, 8}
set2 = {5, 1, 2, 4, 9}  # give 2 sets
print("Given sets:")
print(set1)
print(set2)
un_set = set1.union(set2)
i_set = set1.intersection(set2)
d_set = set1.difference(set2)
s_d_set = set1.symmetric_difference(set2)
print("Union:", un_set)
print("Intersection:", i_set)
print("Difference:", d_set)
print("Symmetric difference:", s_d_set)
print("***************")


print("#3 dictionary creation")
dictionary = {}  # empty dictionary
for n in range(3):  # add key and value 'range()' times
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    dictionary[key] = value  # insert inputs in dictionary
print("Dictionary:", dictionary)
print("***************")


print("#4 dictionary lookup")
d_data = {'A': "Azamat, 17 yo",
          'I': "Ilyas, 8 yo",
          'T': "Takhir, 12 yo"}  # give dictionary
print("Given dictionary:", d_data)
lookup = input("Enter a key to check: ")
if lookup in d_data:  # if key exists in dictionary
    print("The key exists:", d_data[lookup])
else:
    print("The key not found")
print("***************")


print("#5 frequency counter")
i_string = input("Enter a string: ")
c_frequency = {}  # empty char freq
for letter in i_string:  # for each letter in string
    c_frequency[letter] = c_frequency.get(letter, 0) + 1  # count +1 if letter exist
print("Char frequency:", c_frequency)
print("***************")


print("#6 set membership")
set1 = {12, 23, 34, 45, 56, "abc"}
print("Given set:", set1)
set_text = ', '.join(map(str, set1))  # convert elements in set to text to work with any set
checker = input("Enter an element to find: ")
if checker in set_text:  # if element in set
    print(f"The element '{checker}'is in set")
else:
    print(f"The element '{checker}' is not in set")
print("***************")


print("#7 dictionary values")
d_data2 = {'Azamat': 17,
           'Ilyas': 8,
           'Takhir': 12}
print("Given dictionary:", d_data2)
print("All values in dictionary are: ", list(d_data2.values()))  # .values to find values
print("***************")


print("#8 merge dictionaries")
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print("First dictionary is: ", dict1)
print("Second dictionary is: ", dict2)
merged = {**dict1, **dict2}  # merging dictionaries together
print("Merged Dictionary:", merged)
print("***************")


print("#9 dictionary key removal")
d_data1 = {'Azamat': 17,
           'Ilyas': 8,
           'Takhir': 12}
print("Given dictionary is: ", d_data1)
removal = input("Enter the key to be removed: ")
d_data1.pop(removal, None)  # remove entered element
print("After removal: ", d_data1)
print("***************")


print("#10 unique elements")
l_elements = [1, 2, 3, 4, 8, 7, 2, 3, 7]
print("Given list:", l_elements)
u_elements = set(l_elements)  # show repeated elements once
print("Unique Elements set: ", u_elements)
print("***************")
