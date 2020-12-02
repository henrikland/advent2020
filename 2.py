import sys

indata = sorted([int(line.rstrip()) for line in sys.stdin])

def findThree(arr, target):
  length = len(arr)

  for i, inum in enumerate(arr):
    p1 = i + 1
    p2 = length - 1

    for _ in indata[p1:p2]:
      startnum = indata[p1]
      endnum = indata[p2]
      sum = inum + startnum + endnum
      if sum == target:
        return (inum, startnum, endnum)
      elif sum > target:
        p2 -= 1
      else:
        p1 += 1

  return (0, 0, 0)

triple = findThree(indata, 2020)

print("%d + %d + %d = %d" %(triple[0], triple[1], triple[2], (triple[0] * triple[1] * triple[2])))
