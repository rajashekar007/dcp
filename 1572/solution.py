
def allStrings(digits, cur, i, num2char, n, all):
  if i == n:
    all.append(cur)
  else:
    for c in num2char[digits[i]]:
      allStrings(digits, cur+c, i+1, num2char, n, all)


if __name__ == "__main__":
  digit_to_letters = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
  }
  s = input()
  all = []
  allStrings(s, "", 0, digit_to_letters, len(s), all)
  print(all)
  