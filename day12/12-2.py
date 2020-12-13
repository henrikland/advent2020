import sys

class Waypoint:
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

    def rotate_left(self, degrees):
        for _ in range(int(degrees / 90)):
            temp_x = self.x
            temp_y = self.y

            self.y = temp_x
            self.x = -temp_y

    def rotate_right(self, degrees):
        for _ in range(int(degrees / 90)):
            temp_x = self.x
            temp_y = self.y

            self.y = -temp_x
            self.x = temp_y


class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_towards_waypoint(self, waypoint, steps):
        for _ in range(steps):
            self.x += waypoint.x
            self.y += waypoint.y


waypoint = Waypoint(10, 1)
ship = Ship(0, 0)

actions = {
    "N": lambda v: waypoint.move_north(v),
    "S": lambda v: waypoint.move_south(v),
    "E": lambda v: waypoint.move_east(v),
    "W": lambda v: waypoint.move_west(v),
    "L": lambda v: waypoint.rotate_left(v),
    "R": lambda v: waypoint.rotate_right(v),
    "F": lambda v: ship.move_towards_waypoint(waypoint, v)
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
