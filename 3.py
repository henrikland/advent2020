import sys
from functools import reduce

indata = [line.rstrip() for line in sys.stdin]


def isValid(line):
    [policy, password] = line.split(": ")
    [nums, char] = policy.split()
    [min, max] = map(lambda s: int(s), nums.split("-"))
    numchars = reduce(lambda a, s: a + len(s), password.split(char), 0)
    matches = len(password) - numchars
    return matches >= min and matches <= max


count = 0

for line in indata:
    count += 1 if isValid(line) else 0

print(count)
