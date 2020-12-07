import sys
import re

def parseRule(rule):
  cleaned_rule = re.sub(r"( \d )|\sbags?\s?\.?|no other bags\.", "", rule)
  [node, children] = cleaned_rule.split("contain")
  return (node, None if len(children.strip()) == 0 else children.split(","))

nodes = {}

for rule in sys.stdin.read().split("\n"):
  (node, children) = parseRule(rule)
  nodes[node] = children

def findShinyGold(node):
  if node == "shiny gold":
    return 1

  children = nodes[node]

  if children is None:
    return 0

  return any(findShinyGold(child) for child in children)

print(sum([findShinyGold(key) for key in nodes]) - 1) # -1 because we don't count the shiny gold bag
