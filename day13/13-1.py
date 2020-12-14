import sys

lines = sys.stdin.read().split("\n")

timestamp = int(lines[0])
earliest = min(
    map(
        lambda id: (int(id), int(id) - timestamp % int(id)),
        filter(
            lambda id: id != "x",
            lines[1].split(",")
        )
    ),
    key = lambda b: b[1]
)

print(earliest[0] * earliest[1])
