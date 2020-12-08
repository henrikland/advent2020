import sys

def parseInstruction(instruction):
  [op, arg] = instruction.split(" ")
  return (op, arg)

original_instructions = list(
  map(lambda i: parseInstruction(i), sys.stdin.read().split("\n"))
)

def change(instruction):
  (op, arg) = instruction
  return ("nop" if op == "jmp" else "jmp", arg)

def testInstructions(instructions):
  visited = []
  acc = 0
  index = 0

  while index < len(instructions):
    if index in visited:
      return None

    visited.append(index)
    (op, arg) = instructions[index]

    if (op == "acc"):
      acc += int(arg)
    elif (op == "jmp"):
      index += int(arg)
      continue

    index += 1
  
  return acc

for i, instruction in enumerate(original_instructions):
  if instruction[0] == "acc":
    continue
  
  modified_instructions = original_instructions.copy()
  modified_instructions[i] = change(instruction)
  
  result = testInstructions(modified_instructions)
  
  if result is not None:
    print(result)
    break
