use std::io::{self, Read};

fn parse_input(input: &String) -> Vec<i64> {
  input
    .split("\n")
    .map(|line| line.parse::<i64>().unwrap())
    .collect::<Vec<i64>>()
}

fn find_sum(sum: i64, numbers: &Vec<i64>, start: usize, end: usize) -> bool {
  for i in numbers[start..end].iter() {
    for j in numbers[start..end].iter() {
      if i + j == sum && i != j {
        return true;
      }
    }
  }

  false
}

fn main() {
  let mut buffer = String::new();
  io::stdin()
    .read_to_string(&mut buffer)
    .expect("Failed to read from stdin");
  let numbers = parse_input(&buffer);

  for (index, number) in numbers[25..].iter().enumerate() {
    if !find_sum(*number, &numbers, index, index + 25) {
      println!("{}", number);
      break;
    }
  }
}
