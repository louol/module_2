numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()
for i in range(len(numbers)):
    if numbers[i] > 1:
        is_prime = 0
        for j in range(1, numbers[i] + 1):
            if numbers[i] % j == 0:
                is_prime += 1
        if is_prime <= 2:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
print('Primes:', primes)
print('Not Primes:', not_primes)
