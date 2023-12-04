

def ns(n):
  i = 0
  prev_bit = 0
  ans = 0
  while n:
    cur_bit = n&1
    if cur_bit:
      if prev_bit:
        ans = 1<<(i+1)
        prev_bit = 0
      else:
        ans |= 1<<i
        prev_bit = 1
    else:
      prev_bit = (ans>>i) & 1
      
    i += 1
    n >>= 1
  return ans
  
def next_sparse(n):
  # Initialize result as 0 and previous_bit as 0
  res = 0
  prev_bit = 0
  i = 0

  # While n is not zero
  while n:
    # If current bit is set
    if n & 1:
      # If previous bit is also set, we need to set next bit in result
      if prev_bit:
        res |= 1 << (i+1)
        prev_bit = 0
      else:
        res |= 1 << i
        prev_bit = 1
    # If current bit is not set
    else:
      res |= 0 << i
      prev_bit = 0

    # Right shift n
    n >>= 1
    i += 1

  # If last bit is set, set next bit in result
  if prev_bit:
    res |= 1 << i

  return res
  
def next_sparse_number(n):
    # Convert the number to binary string
    binary = bin(n)[2:]
    binary = list(binary)  # Convert to list for easier manipulation
    
    i = 1
    while i < len(binary):
        # Check for consecutive '1's
        if binary[i] == '1' and binary[i - 1] == '1':
            j = i
            # Find the end of consecutive '1's
            while j < len(binary) and binary[j] == '1':
                j += 1
            
            # Modify the binary representation to make it sparse
            if j < len(binary):
                binary[j] = '1' if binary[j] == '0' else '0'
            else:
                binary.append('0')
        
        i += 1
    
    # Convert the modified binary representation back to decimal
    return int(''.join(binary), 2)

# # Test cases
# print(next_sparse_number(21))  # Output: 21 (10101)
# print(next_sparse_number(22))  # Output: 32 (100000)


if __name__ == "__main__":
  n = int(input())
  print(ns(n))
  print(next_sparse(n))
  print(next_sparse_number(n))
