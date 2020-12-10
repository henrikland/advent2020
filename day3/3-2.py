import sys
from numpy import prod

lines = sys.stdin.read().split('\n')

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

trees = [0 for i in range(len(slopes))]

for i, slope in enumerate(slopes):
    [pos_inc, line_inc] = slope
    line_idx = 0
    step = 0

    while line_idx < len(lines):
        line = lines[line_idx]
        trees[i] += 1 if line[(step * pos_inc) % len(line)] == '#' else 0
        line_idx += line_inc
        step += 1

print(prod(trees))
