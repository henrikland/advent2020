import sys

diff_histogram = {
    1: 0,
    3: 1
}

adapters = [
    0,
    *sorted(map(lambda line: int(line), sys.stdin.read().split("\n")))
]

for i in range(len(adapters) - 1):
    diff_histogram[adapters[i + 1] - adapters[i]] += 1

print(diff_histogram[1] * diff_histogram[3])
