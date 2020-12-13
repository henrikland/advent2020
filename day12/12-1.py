import sys

class Ship:
    directions = ["N", "E", "S", "W"]
    current_direction = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_north(self, steps):
        self.y += steps

    def move_south(self, steps):
        self.y -= steps

    def move_east(self, steps):
        self.x += steps

    def move_west(self, steps):
        self.x -= steps

    def rotate_right(self, degrees):
        self.current_direction = int(
            (self.current_direction + degrees / 90) % 4
        )

    def rotate_left(self, degrees):
        self.current_direction = int(
            (self.current_direction - degrees / 90) % 4
        )

    def move_forward(self, steps):
        actions = {
            "N": self.move_north,
            "E": self.move_east,
            "S": self.move_south,
            "W": self.move_west,
        }

        actions[self.directions[self.current_direction]](steps)

ship = Ship(0, 0)

actions = {
    "N": lambda v: ship.move_north(v),
    "E": lambda v: ship.move_east(v),
    "S": lambda v: ship.move_south(v),
    "W": lambda v: ship.move_west(v),
    "L": lambda v: ship.rotate_left(v),
    "R": lambda v: ship.rotate_right(v),
    "F": lambda v: ship.move_forward(v),
}

instructions = list(
    map(
        lambda instruction: (instruction[0], int(instruction[1:])),
        sys.stdin.read().split("\n")
    )
)

for instruction in instructions:
    (action, value) = instruction
    actions[action](value)

print(abs(ship.x) + abs(ship.y))
