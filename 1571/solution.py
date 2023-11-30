
class Trie:
  def __init__(self) -> None:
    self.children = {}
    self.is_end = False
    
def build_trie(words):
  root = Trie()
  for w in words:
    node = root
    for c in w:
      if c not in node.children:
        node.children[c] = Trie()
      node = node.children[c]
    node.is_end = True
  return root

def word_break(s, words):
  root = build_trie(words)
  n = len(s)
  dp = [None]*(n+1)
  dp[0] = [[]]
  for i in range(n):
    if dp[i] is None:
      continue
    node = root
    for j in range(i, n):
      if s[j] in node.children:
        node = node.children[s[j]]
      else:
        break
      if node.is_end:
        if dp[j+1] is None:
          dp[j+1] = []
        for l in range(len(dp[i])):
          dp[j+1].append(dp[i][l] + [s[i:j+1]])
  return dp[n]

  
if __name__ == "__main__":
  words1 = ['quick', 'brown', 'the', 'fox']
  string1 = "thequickbrownfox"
  print(word_break(string1, words1))  # Output: [['the', 'quick', 'brown', 'fox']]

  # Example 2
  words2 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
  string2 = "bedbathandbeyond"
  print(word_break(string2, words2))  # Output: [['bed', 'bath', 'and', 'beyond'], ['bedbath', 'and', 'beyond']]


  