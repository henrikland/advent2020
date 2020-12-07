import sys
import re

child_group_pattern = re.compile(r"(\d+) ([\w\s]+)")

def parseRule(rule):
  cleaned_rule = re.sub(r"\sbags?\s?\.?|no other bags\.", "", rule)
  [node, contents] = cleaned_rule.split("contain ")
  if len(contents.strip()) == 0:
    return (node, None)

  children = []

  for child in contents.split(", "):
    match = child_group_pattern.match(child)
    children.append((int(match.group(1)), match.group(2)))

  return (node, children)

nodes = {}

for rule in sys.stdin.read().split("\n"):
  (node, children) = parseRule(rule)
  nodes[node] = children

def countBags(key):
  children = nodes[key]
  if children is None:
    return 1

  count = 1

  for child in children:
    count += child[0] * countBags(child[1])

  return count

print(countBags("shiny gold") - 1) # -1 because we don't count the shiny gold bag
