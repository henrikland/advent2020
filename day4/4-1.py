import sys
import re

pattern = re.compile("\w{3}:")

def isValid(passport):
  return len(passport) == 8 or (len(passport) == 7 and not "cid:" in passport)

count = 0

for passport in sys.stdin.read().split("\n\n"):
  count += 1 if isValid(pattern.findall(passport)) else 0

print(count)
