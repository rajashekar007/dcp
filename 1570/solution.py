

def getNextTerm(s):
  i = 0
  n = len(s)
  next = ''
  while i < n:
    j = i
    while j<n and s[j] == s[i]:
      j += 1
    cur_times = str(j-i)
    next += cur_times+s[i]
    i = j
  return next

def getNthTerm(n):
  i = 1
  term = '1'
  while i < n:
    term = getNextTerm(term)
    i += 1
  return term

if __name__ == "__main__":
  n = int(input())
  print(getNthTerm(n))