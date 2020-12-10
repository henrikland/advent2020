import sys

instructions = sys.stdin.read().split("\n")
visited = []
acc = 0
index = 0

while index < len(instructions):
  visited.append(index)
  instruction = instructions[index]
  [op, arg] = instruction.split(" ")
  
  if (op == "acc"):
    acc += int(arg)
  elif (op == "jmp"):
    index += int(arg)

    if index in visited:
      print(acc)
      break

    continue

  index += 1
