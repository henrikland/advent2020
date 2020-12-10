use std::io::{self, Read};

enum Op {
  Acc,
  Jmp,
  Nop
}

struct Instruction {
  op: Op,
  arg: i32
}

fn parse_instruction(instruction: &str) -> Instruction {
  let split: Vec<&str> = instruction.split(" ").collect();

  Instruction {
    op: match split[0] {
      "acc" => Op::Acc,
      "jmp" => Op::Jmp,
      "nop" => Op::Nop,
      _ => panic!("Bad input op: {}", split[0])
    },
    arg: split[1].parse::<i32>().unwrap()
  }
}

fn parse_boot_code(boot_code: &String) -> Vec<Instruction> {
  boot_code
    .split("\n")
    .map(|instruction| parse_instruction(&instruction))
    .collect::<Vec<Instruction>>()
}

fn main() {
  let mut buffer = String::new();
  io::stdin()
    .read_to_string(&mut buffer)
    .expect("Failed to read from stdin");

  let instructions = parse_boot_code(&buffer);

  let mut visited: Vec<i32> = vec![];
  let mut index: i32 = 0;
  let mut acc: i32 = 0;

  while (index as usize) < instructions.len() {
    visited.push(index);
    let instruction: &Instruction = &instructions[index as usize];

    match instruction.op {
      Op::Acc => acc += instruction.arg,
      Op::Jmp => {
        index += instruction.arg;

        if visited.contains(&index) {
          break;
        }

        continue;
      },
      _ => ()
    }

    index += 1;
  }

  println!("{}", acc)
}
