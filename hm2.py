user_input = input("Enter numbers separated by comma: ")

list = user_input.split(',')
if len(list) == 1 and list[0] == '':
    first_half = []
    second_half = []
else:
    middle = len(list) // 2
    first_half = list[:middle + len(list) % 2]
    second_half = list[middle + len(list) % 2:]

print("First list :", first_half)
print("Second list :", second_half)
