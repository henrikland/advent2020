import sys
import re

replacers = {
  "F": "0",
  "L": "0",
  "B": "1",
  "R": "1",
}

max_seat = 0

for boarding_pass in sys.stdin.read().split("\n"):
  bin_str = re.sub(r"[FBLR]", lambda c: replacers[c.group(0)], boarding_pass)
  seat = int(bin_str, 2)
  if seat > max_seat:
    max_seat = seat

print("%d" %max_seat)
