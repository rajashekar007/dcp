def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    
    primes = [i for i in range(2, n + 1) if sieve[i]]
    return primes

def generate_primes():
    sieve = {}
    num = 2
    while True:
        if num not in sieve:
            yield num
            sieve[num * num] = [num]
        else:
            print(num)
            print(sieve)
            for p in sieve[num]:
                sieve.setdefault(p + num, []).append(p)
            del sieve[num]
        num += 1

# Finding primes less than 100
primes_less_than_100 = sieve_of_eratosthenes(100)
print("Primes less than 100:", primes_less_than_100)

# Generating primes indefinitely
prime_generator = generate_primes()
print("First 10 primes:")
for _ in range(10):
    print(next(prime_generator))
