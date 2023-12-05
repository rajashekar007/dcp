class TrieNode:
  def __init__(self) -> None:
    self.children = {}
    self.is_end = True
    self.prefix_cnt = {}
    
def build_trie(words):
  root = TrieNode()
  for w in words:
    node = root
    for c in w:
      if c not in node.children:
        node.children[c] = TrieNode()
        node.prefix_cnt[c] = 0
      node.prefix_cnt[c] += 1
      node = node.children[c]
    node.is_end = True
  return root

def get_uniqe_prefix(trie, w):
  node = trie
  prefix = ''
  for c in w:
    prefix += c
    # print(w, c)
    if node.prefix_cnt[c] == 1:
      return prefix
    node = node.children[c]
  return ''
      

def uniqe_prefixes(words):
  trie = build_trie(words)
  prefixes = []
  for w in words:
    prefixes.append(get_uniqe_prefix(trie, w))
  return prefixes

if __name__ == "__main__":
  words = ["dog", "cat", "apple", "apricot", "fish"]
  prefixes = uniqe_prefixes(words)
  print(prefixes)
  