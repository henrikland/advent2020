import sys
import re

mask_group_pattern = re.compile(r"mask = ([X01]{36})")
write_group_pattern = re.compile(r"mem\[(\d+)\] = (\d+)")


def parse_mask(mask_str):
    return mask_group_pattern.match(mask_str).group(1)


def parse_write(write_str):
    match = write_group_pattern.match(write_str)
    return (int(match.group(1)), int(match.group(2)))


def get_mask_variations(mask):
    char = mask[0]
    char_variations = ["0", "1"] if char == "X" else [char]

    if len(mask) == 1:
        return char_variations

    variations = []
    next_variations = get_mask_variations(mask[1:])

    for p in char_variations:
        for np in next_variations:
            variations.append(p + np)

    return variations


def write_with_mask(memory, mask, address, value):
    # We set the zeroes in the mask to ones and the floating bits to zeroes...
    clear_mask = mask.replace("0", "1").replace("X", "0")
    # ...then use that to remove the floating bits from the address since they don't matter
    cleared_address = address & int(clear_mask, 2)

    mask_variations = get_mask_variations(mask)

    for variation in mask_variations:
        memory[cleared_address | int(variation, 2)] = value


program = sys.stdin.read().split("\n")

current_mask = parse_mask(program[0])
memory = {}

for line in program[1:]:
    if line.startswith("mask"):
        current_mask = parse_mask(line)
    else:
        (address, value) = parse_write(line)
        write_with_mask(memory, current_mask, address, value)

print(sum(memory.values()))
