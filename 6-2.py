import sys

questions = list("abcdefghijklmnopqrstuvwxyz")

def countAnswersInGroup(group):
  num_people = len(group.split("\n"))
  answers = 0

  for q in questions:
    answers += 1 if group.count(q) == num_people else 0

  return answers

count = 0

for group in sys.stdin.read().split("\n\n"):
  count += countAnswersInGroup(group)

print(count)
