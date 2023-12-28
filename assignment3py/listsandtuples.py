print("#1 list creation")
fruits = []  # create empty list
for f in range(5):  # range of amount of repetition of input
    fruit = input("Enter favourite fruit: ")
    fruits.append(fruit)  # collect all inputs in list
print("List of fruits: ", fruits)  # output of the list
print("**********************")


print("#2 list slicing")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # given list
slicing = list1[2:7]  # by slicing method take 5 number from middle
# since there is 10 numbers in the list I started middle from 2 index(3rd number)
# and ended after collected 5 elements
print("Middle five elements: ", slicing)
print("**********************")


print("#3 tuple conversion")
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
input3 = int(input("Enter third number: "))  # enter three numbers separately
numbers = (input1, input2, input3)  # storing in tuple
print(numbers)
print("**********************")


print("#4 list operations")
list_ex = list(map(int, input("Enter a list of nums separated by space: ").split()))
list_app = int(input("Enter a number to add in the end: "))
list_ex.append(list_app)  # adds number in the end
print("Added number in the end: ", list_ex)
list_ex.pop(0)  # removes first element
print("Removed first item: ", list_ex)
list_ex.sort()  # sorts
print("Sorted list: ", list_ex)  # output
print("**********************")


print("#5 element search")
list_f = list(map(int, input("Enter a list of nums separated by space: ").split()))
search = int(input("Enter a number to search in list: "))
if search in list_f:  # searches number in list
    print(f"The number {search} is in the list")
else:  # if number not in list
    print(f"The number {search} is not in the list")
print("**********************")


print("#5 list reversal")
list_r = list(map(int, input("Enter a list of nums separated by space: ").split()))
print("Entered list", list_r)
list_r.reverse()  # reverses the list
print("Reversed list", list_r)
print("**********************")


print("#7 tuple unpacking")
tuple_u = tuple(map(int, input("Enter 4 numbers separated by space: ").split()))
print("Tuple:", tuple_u)
a, b, c, d = tuple_u
print("Unpacked elements of tuple:", a, b, c, d)
print("**********************")


print("8 maximum and minimum")
u_input = list(map(int, input("Enter the list of nums separated by space: ").split()))
max_num = max(u_input)
min_num = min(u_input)
print("Maximum number:", max_num)
print("Minimum number:", min_num)
print("**********************")


print("#9 concatenate lists")
list1 = list(map(int, input("Enter the list of nums separated by space: ").split()))
list2 = list(map(int, input("Enter the list of nums separated by space: ").split()))
c_list = list1 + list2
print("Concatenated list:", c_list)
print("**********************")


print("#10 list to tuple")
user_input = list(map(int, input("Enter the list of nums separated by space: ").split()))
print(user_input)
user_tuple = tuple(user_input)
print("Converted tuple:", user_tuple)
print("**********************")
