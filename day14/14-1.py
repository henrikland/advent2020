import sys
import re

mask_group_pattern = re.compile(r"mask = ([X01]{36})")
write_group_pattern = re.compile(r"mem\[(\d+)\] = (\d+)")


def parse_mask(mask_str):
    mask = mask_group_pattern.match(mask_str).group(1)

    return {
        "AND": int(mask.replace("X", "1"), 2),
        "OR": int(mask.replace("X", "0"), 2)
    }


def parse_write(write_str):
    match = write_group_pattern.match(write_str)
    return (int(match.group(1)), int(match.group(2)))


program = sys.stdin.read().split("\n")

current_masks = parse_mask(program[0])
memory = {}

for line in program[1:]:
    if line.startswith("mask"):
        current_masks = parse_mask(line)
    else:
        (address, value) = parse_write(line)
        memory[address] = value & current_masks["AND"] | current_masks["OR"]

print(sum(memory.values()))
