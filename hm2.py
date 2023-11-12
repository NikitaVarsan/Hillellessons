while True:
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    Action = input("Enter Action: ")

    if Action == "+":
        print(first_num + second_num)
    elif Action == "-":
        print(first_num - second_num)
    elif Action == "*":
        print(first_num * second_num)
    elif Action == "/":
        if second_num == 0:
            print("You can't divide by 0")
        else:
            print(first_num / second_num)

    question = input("Do you want to continue (yes/no): ")
    if question != "yes":
        print("Have a nice day!!!!!")
        break



