

def findPivot(srl): #sortedRotatedList
  high = len(srl)
  low = 0
  while True:
    mid = low + (high - low)//2
    if srl[mid] < srl[mid+1] and srl[mid] < srl[mid-1]:
      return srl[mid]
    elif srl[low] < srl[mid]:
      low = mid + 1
    else:
      high = mid - 1
  return srl[mid]

if __name__ == "__main__":
  srl = [7, 8, 9, 2, 3, 4, 5]
  print(findPivot(srl))
    
  