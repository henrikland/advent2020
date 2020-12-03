import sys

pos = 3
trees = 0
for i, line in enumerate(sys.stdin.read().split('\n')):
    trees += 1 if line[(i * pos) % len(line)] == '#' else 0

print(trees)
