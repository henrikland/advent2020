import sys
import re

passport_pattern = re.compile("\w{3}:[^\s]+")
cid_pattern = re.compile("cid:[^\s]+")

hcl_rule_pattern = re.compile("^#[a-f0-9]{6}$")
pid_rule_pattern = re.compile("^[0-9]{9}$")

hgt_group_pattern = re.compile("^(\d+)(\w+)$")

def isValidHeight(height):
  match = hgt_group_pattern.match(height)

  if not match:
    return False

  value = int(match.group(1))
  unit = match.group(2)

  if unit == "cm":
    return value >= 150 and value <= 193

  return value >= 59 and value <= 76

rules = {
  "byr": lambda b: int(b) >= 1920 and int(b) <= 2002,
  "iyr": lambda y: int(y) >= 2010 and int(y) <= 2020,
  "eyr": lambda y: int(y) >= 2020 and int(y) <= 2030,
  "hgt": lambda h: isValidHeight(h),
  "hcl": lambda h: hcl_rule_pattern.match(h),
  "ecl": lambda e: e in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
  "pid": lambda p: pid_rule_pattern.match(p),
  "cid": lambda c: True
}

def isValid(passport):
  if not (len(passport) == 8 or (len(passport) == 7 and len(list(filter(lambda p: cid_pattern.match(p), passport))) == 0)):
    return False

  for field in passport:
    [key, value] = field.split(":")
    if not rules[key](value):
      return False

  return True

count = 0

for passport in sys.stdin.read().split("\n\n"):
  count += 1 if isValid(passport_pattern.findall(passport)) else 0

print(count)
