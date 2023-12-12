

def seive_of_eratosthenes(N : int) -> [int]:
  numbers = [1]*(N+1)
  primes = []
  for i in range(2, N+1):
    if numbers[i]:
      primes.append(i)
      for j in range(2*i, N+1, i):
        numbers[j] = 0
  return primes


if __name__ == "__main__":
  p = seive_of_eratosthenes(1000)
  print(p)