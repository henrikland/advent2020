import sys
import re

replacers = {
  "F": "0",
  "L": "0",
  "B": "1",
  "R": "1",
}

def parseBoardingPass(bp):
  bin_str = re.sub(r"[FBLR]", lambda c: replacers[c.group(0)], bp)
  return int(bin_str, 2)

sorted_seats = sorted(map(lambda bp: parseBoardingPass(bp), sys.stdin.read().split("\n")))

for i, seat in enumerate(sorted_seats):
  if sorted_seats[i + 1] - sorted_seats[i] is not 1:
    print(seat + 1)
    break
