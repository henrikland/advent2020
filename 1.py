import sys

indata = [int(line.rstrip()) for line in sys.stdin]

length = 2021
arr = [0 for i in range(length)]

for num in indata:
  arr[num] = 1

pair = (0, 0)

for idx, num in enumerate(arr):
  if num == 1 and arr[length - 1 - idx] == 1:
    pair = (idx, length - 1 - idx)
    break

print("%d + %d = %d" %(pair[0], pair[1], (pair[0] * pair[1])))
