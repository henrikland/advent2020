import sys
import re

range_group_pattern = re.compile(r".+: (\d+)-(\d+) or (\d+)-(\d+)")


def parse_ranges(ranges_str):
    lines = ranges_str.split("\n")

    ranges = []

    for line in lines:
        match = range_group_pattern.match(line)

        for i in range(1, 4, 2):
            ranges.append(
                (
                    int(match.group(i)),
                    int(match.group(i + 1))
                )
            )

    return ranges


def parse_nearby_tickets(tickets_str):
    return list(
        map(
            lambda n: int(n),
            tickets_str.split(":\n")[1].replace("\n", ",").split(",")
        )
    )


sections = sys.stdin.read().split("\n\n")

ranges = parse_ranges(sections[0])
fields = parse_nearby_tickets(sections[2])

print(
    sum(
        filter(
            lambda field: not any(range[0] <= field <= range[1]
                                  for range in ranges),
            fields
        )
    )
)
