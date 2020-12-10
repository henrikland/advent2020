import sys


def isValid(line):
    [policy, password] = line.split(": ")
    [nums, char] = policy.split()
    [min, max] = map(lambda s: int(s), nums.split("-"))
    count = password.count(char)
    return count >= min and count <= max


count = 0

for line in sys.stdin.read().split('\n'):
    count += 1 if isValid(line) else 0

print(count)
