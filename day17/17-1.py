import sys
import math

lines = sys.stdin.read().split("\n")

LENGTH = len(lines[0])
ITERATIONS = 6
LENGTH_WITH_SPACE = LENGTH + 3 * ITERATIONS
MIDDLE_INDEX = math.ceil(LENGTH_WITH_SPACE / 2)


def new_grid():
    return [
        [
            [
                False for _ in range(LENGTH_WITH_SPACE)
            ] for _ in range(LENGTH_WITH_SPACE)
        ] for _ in range(LENGTH_WITH_SPACE)
    ]


grid = new_grid()

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        grid[MIDDLE_INDEX + x][MIDDLE_INDEX + y][MIDDLE_INDEX] = char == "#"


def check_cube(grid, cube_x, cube_y, cube_z):
    cube_active = grid[cube_x][cube_y][cube_z]

    active_neighbors = 0
    neighbors = [-1, 0, 1]

    for x in neighbors:
        for y in neighbors:
            for z in neighbors:
                if x == 0 and y == 0 and z == 0:
                    continue

                neighbor_x = cube_x + x
                neighbor_y = cube_y + y
                neighbor_z = cube_z + z

                x_outside = neighbor_x < 0 or neighbor_x > LENGTH_WITH_SPACE - 1
                y_outside = neighbor_y < 0 or neighbor_y > LENGTH_WITH_SPACE - 1
                z_outside = neighbor_z < 0 or neighbor_z > LENGTH_WITH_SPACE - 1

                if x_outside or y_outside or z_outside:
                    continue

                if grid[neighbor_x][neighbor_y][neighbor_z]:
                    active_neighbors += 1

                    if active_neighbors > 3:
                        return False

    return 2 <= active_neighbors <= 3 if cube_active else active_neighbors == 3


for i in range(ITERATIONS):
    fresh_grid = new_grid()

    for x in range(LENGTH_WITH_SPACE):
        for y in range(LENGTH_WITH_SPACE):
            for z in range(LENGTH_WITH_SPACE):
                fresh_grid[x][y][z] = check_cube(grid, x, y, z)

    grid = fresh_grid

count = 0

for x in range(LENGTH_WITH_SPACE):
    for y in range(LENGTH_WITH_SPACE):
        for z in range(LENGTH_WITH_SPACE):
            if grid[x][y][z]:
                count += 1

print(count)
