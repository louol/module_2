
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = 0
while number <= len(my_list) - 1:
    if my_list[number] < 0:
        break
    elif my_list[number] == 0:
        number = number + 1
        continue
    print(my_list[number])
    number = number + 1