number = int(input("Enter a 4 digit number: "))


first_num = number // 1000
second_num = (number % 1000) // 100
third_num = (number % 100) // 10
fourth_num = number % 10

print(first_num)
print(second_num)
print(third_num)
print(fourth_num)