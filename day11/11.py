import sys
from copy import deepcopy

seats = list(
    map(
        lambda row: list(row),
        sys.stdin.read().split("\n")
    )
)
num_cols = len(seats[0])
num_rows = len(seats)

cache_neighbors = [
    [
        None for _ in range(num_cols)
    ] for _ in range(num_rows)
]

def in_range(value, min, max):
    return min <= value <= max

def check_direction(row, column, dx, dy, depth):
    new_row = row + dy
    new_col = column + dx
    number_iterations = 0

    while (
        number_iterations < depth and
        in_range(new_row, 0, num_rows - 1) and
        in_range(new_col, 0, num_cols - 1)
    ):
        if (seats[new_row][new_col] != "."):
            return (new_row, new_col)

        new_row += dy
        new_col += dx
        number_iterations += 1

    return None

def neighbors_for_cell(row, column, depth):
    if cache_neighbors[row][column] is not None:
        return cache_neighbors[row][column]

    neighbors = list(
        filter(
            lambda direction: direction != None,
            map(
                lambda d: check_direction(row, column, d[0], d[1], depth),
                [
                    (-1, -1), (0, -1), (1, -1),
                    (-1, 0), (1, 0),
                    (-1, 1), (0, 1), (1, 1)
                ]
            )
        )
    )

    cache_neighbors[row][column] = neighbors

    return neighbors


def mutate(grid, max_occupied, depth):
    changed = False
    new_grid = deepcopy(grid)

    for row in range(len(grid)):
        for col, char in enumerate(grid[row]):
            if char == ".":
                new_grid[row][col] = char
                continue

            occupied = list(
                map(
                    lambda cell: grid[cell[0]][cell[1]],
                    neighbors_for_cell(row, col, depth)
                )
            ).count("#")

            if char == "L" and occupied == 0:
                new_grid[row][col] = "#"
                changed = True
            elif char == "#" and occupied > max_occupied:
                new_grid[row][col] = "L"
                changed = True

    return (new_grid, changed)

def get_number_of_occupied_seats(seats, max_occupied, depth):
    while True:
        (new_seats, changed) = mutate(seats, max_occupied, depth)
        seats = new_seats
        if not changed:
            break

    return sum(
        map(
            lambda row: row.count("#"),
            seats
        )
    )

orig_seats = deepcopy(seats)
orig_cache = deepcopy(cache_neighbors)

print("Occupied seats for day 1: %d" % get_number_of_occupied_seats(seats, 3, 1))

seats = orig_seats
cache_neighbors = orig_cache

print("Occupied seats for day 2: %d" % get_number_of_occupied_seats(seats, 4, num_rows))
