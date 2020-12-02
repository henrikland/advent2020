import sys
from functools import reduce

indata = [line.rstrip() for line in sys.stdin]


def isValid(line):
    [policy, password] = line.split(": ")
    [nums, char] = policy.split()
    [p1, p2] = map(lambda s: int(s), nums.split("-"))
    return (password[p1 - 1] == char) ^ (password[p2 - 1] == char)


count = 0

for line in indata:
    count += 1 if isValid(line) else 0

print(count)
