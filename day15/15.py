import sys

starting_numbers = list(map(lambda n: int(n), sys.stdin.read().split(",")))

last_indices = {}

for i, n in enumerate(starting_numbers[0:-1]):
    last_indices[n] = i

count = len(starting_numbers)
last_number = starting_numbers[len(starting_numbers) - 1]

while count < 30000000:
    next_number = 0

    if last_number in last_indices.keys():
        next_number = (count - 1) - last_indices[last_number]

    last_indices[last_number] = count - 1
    last_number = next_number
    count += 1

    if count == 2020:
        print("2020th: %d" % last_number)

print("30000000th: %d" % last_number)
