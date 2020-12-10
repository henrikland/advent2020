import sys

questions = list("abcdefghijklmnopqrstuvwxyz")

def countAnswersInGroup(group):
  answers = 0

  for q in questions:
    answers += 1 if q in group else 0

  return answers

count = 0

for group in sys.stdin.read().split("\n\n"):
  count += countAnswersInGroup(group)

print(count)
