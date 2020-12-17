import sys
import re

range_group_pattern = re.compile(r".+: (\d+)-(\d+) or (\d+)-(\d+)")


def parse_ranges(ranges_str):
    lines = ranges_str.split("\n")

    ranges = []

    for line in lines:
        match = range_group_pattern.match(line)
        range_pair = (
            (
                int(match.group(1)),
                int(match.group(2)),
            ),
            (
                int(match.group(3)),
                int(match.group(4)),
            )
        )
        ranges.append(range_pair)

    return ranges


def parse_your_ticket(ticket_str):
    return list(
        map(
            lambda n: int(n),
            ticket_str.split(":\n")[1].split(",")
        )
    )


def parse_nearby_tickets(tickets_str):
    return list(
        map(
            lambda line: [int(n) for n in line.split(",")],
            tickets_str.split(":\n")[1].split("\n")
        )
    )


def in_range(value, range_pair):
    (min1, max1) = range_pair[0]
    (min2, max2) = range_pair[1]
    return min1 <= value <= max1 or min2 <= value <= max2


def is_ticket_valid(ticket, ranges):
    for field in ticket:
        if not any(in_range(field, range_pair) for range_pair in ranges):
            return False

    return True


sections = sys.stdin.read().split("\n\n")

ranges = parse_ranges(sections[0])
your_ticket = parse_your_ticket(sections[1])
nearby_tickets = parse_nearby_tickets(sections[2])

valid_tickets = list(
    filter(
        lambda ticket: is_ticket_valid(ticket, ranges),
        nearby_tickets
    )
)

correct_fields = [[] for _ in valid_tickets[0]]

fields_for_index = list(zip(*valid_tickets))

for i_r, range_pair in enumerate(ranges):
    for i_v, fields in enumerate(fields_for_index):
        if all(in_range(field, range_pair) for field in fields):
            correct_fields[i_v].append(i_r)


singles = [None for _ in valid_tickets[0]]

while any(s is None for s in singles):
    for i, field in enumerate(correct_fields):
        if len(field) == 1:
            singles[i] = (i, field)

    for s in filter(lambda s: s is not None, singles):
        (index, r) = s

        for j, f in enumerate(correct_fields):
            if j != index and r[0] in f:
                f.remove(r[0])

product = 1

for i, c in enumerate(correct_fields):
    if 0 <= c[0] <= 5:
        product *= your_ticket[i]

print(product)
