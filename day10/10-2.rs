use std::io::{self, Read};
use std::cmp::min;

fn parse_input(input: &String) -> Vec<u32> {
  input
    .split("\n")
    .map(|line| line.parse::<u32>().unwrap())
    .collect::<Vec<u32>>()
}

fn paths_for_index(adapter_index: usize, adapters: &Vec<u32>, cache: &mut Vec<u64>) -> u64 {
  if cache[adapter_index] != 0 {
    return cache[adapter_index];
  }

  if adapter_index == adapters.len() - 2 {
    return 1;
  }

  let paths_for_adapter: u64 = ((adapter_index + 1)..min(adapter_index + 4, adapters.len()))
    .filter(|index| adapters[*index] - adapters[adapter_index] < 4)
    .map(|index| paths_for_index(index, adapters, cache))
    .sum();

  cache[adapter_index] = paths_for_adapter;
  paths_for_adapter
}

fn main() {
  let mut buffer = String::new();
  io::stdin()
    .read_to_string(&mut buffer)
    .expect("Failed to read from stdin");

  let mut numbers = parse_input(&buffer);
  numbers.sort_unstable();
  numbers.insert(0, 0);
  numbers.push(numbers.last().unwrap() + 3);

  let mut cache_paths: Vec<u64> = vec![0; numbers.len()];

  println!("{}", paths_for_index(0, &numbers, &mut cache_paths));
}
