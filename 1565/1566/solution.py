
def PalindromeLength(s, i, j, n):
  len = 0
  while i>=0 and j<n:
    if s[i] == s[j]:
      len += 1 if i == j else 2
    else:
      return (len, i+1, j-1)
    i -= 1
    j += 1
  return (len, i+1, j-1)

def LongestPalindromicSubstring(s):
  ans = ''
  maxlen = 0
  n = len(s)
  for i in range(1, n):
    (len1, start1, end1) = PalindromeLength(s, i, i, n)
    (len2, start2, end2) = PalindromeLength(s, i, i, n)
    if len1 > maxlen:
      maxlen,ans = len1, s[start1:end1+1]
    if len2 > maxlen:
      maxlen,ans = len2, s[start2:end2+1]
  return ans

def solve(s):
  return LongestPalindromicSubstring(s)

if __name__ == "__main__":
  s = input()
  ans = solve(s)
  print(ans)
  