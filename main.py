import random
my_list = [random.randint(0,9 )
for i in range(random.randint(3, 10))]


first_number = my_list[0]
third_number = my_list[2]
second_from_end_number = my_list[-2]

print(my_list)
print(first_number, third_number, second_from_end_number)