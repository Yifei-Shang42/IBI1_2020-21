# pseudocode:
# 
# create a list to carry the sequence
# create an integer to count number of numbers in the list
# while number of numbers in the list is less than 13:
#     append the sum of last 2 numbers to the list
#     add 1 to number count
# print all numbers in the list one by one 

list_of_numbers = [1, 1]
i = 2
while i < 13:
    list_of_numbers.append(list_of_numbers[i-2] + list_of_numbers[i-1])
    i += 1
for i in list_of_numbers:
    print(i)
