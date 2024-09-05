while True:
    n = int(input('Введите число от 3 до 20 :'))
    if n < 3 or n > 20:
        print('Число не подходит')
        continue
    else:
        break
result = list()
for i in range(1, n):
    for j in range(2, n):
        if (i != j) and (n % (i + j)) == 0 and (i < j):
           result.append(i)
           result.append(j)
print(n,' - ', *result)
