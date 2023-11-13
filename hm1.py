List = [0, 1, 7, 2, 4, 8]
if not List:
    result = 0
else:
    even_sum = 0
    for i in range(0, len(List), 2):
        even_sum += List[i]
    result = even_sum * List[-1]
print(result)


List = [1, 3, 5]
if not List:
    result = 0
else:
    even_sum = 0
    for i in range(0, len(List), 2):
        even_sum += List[i]
    result = even_sum * List[-1]
print(result)


List = [6]
if not List:
    result = 0
else:
    even_sum = 0
    for i in range(0, len(List), 2):
        even_sum += List[i]
    result = even_sum * List[-1]
print(result)

List = []
if not List:
    result = 0
else:
    even_sum = 0
    for i in range(0, len(List), 2):
        even_sum += List[i]
    result = even_sum * List[-1]
print(result)
