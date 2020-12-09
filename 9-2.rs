use std::io::{self, Read};
use std::cmp::Ordering;

fn parse_input(input: &String) -> Vec<i64> {
  input
    .split("\n")
    .map(|line| line.parse::<i64>().unwrap())
    .collect::<Vec<i64>>()
}

fn find_sum(target_sum: i64, numbers: &Vec<i64>, start: usize, end: usize) -> bool {
  for i in numbers[start..end].iter() {
    for j in numbers[start..end].iter() {
      if i + j == target_sum && i != j {
        return true;
      }
    }
  }

  false
}

fn find_contiguous_sum(target_sum: i64, numbers: &Vec<i64>, start: usize, end: usize) -> Option<Vec<i64>> {
  for (i, number) in numbers[start..end - 1].iter().enumerate() {
    let mut sum: i64 = *number;
    let mut j = i + 1;

    loop {
      match sum.cmp(&target_sum) {
        Ordering::Less => {
          sum += numbers[j];
          j += 1;
        },
        Ordering::Greater => break,
        Ordering::Equal => return Some(numbers[i..j].to_vec()),
      }
    }
  }

  None
}

fn main() {
  let mut buffer = String::new();
  io::stdin()
    .read_to_string(&mut buffer)
    .expect("Failed to read from stdin");

  let numbers = parse_input(&buffer);
  let mut invalid_number: Option<i64> = None;

  for (index, number) in numbers[25..].iter().enumerate() {
    if !find_sum(*number, &numbers, index, index + 25) {
      invalid_number = Some(*number);
      break;
    }
  }

  if let None = invalid_number {
    panic!("Found no invalid number");
  }

  let invalid_number = invalid_number.unwrap();
  let invalid_number_index = numbers
    .iter()
    .position(|number| *number == invalid_number)
    .unwrap();

  let mut terms = find_contiguous_sum(invalid_number, &numbers, 0, invalid_number_index).unwrap();
  terms.sort_unstable();

  println!("{}", terms[0] + terms[terms.len() - 1]);
}
