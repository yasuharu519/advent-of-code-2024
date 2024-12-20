use regex::Regex;
use std::io;

fn main() {
    let pattern = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)").unwrap();
    let stdin = io::stdin();
    let mut result = 0;

    for line in stdin.lines() {
        let line = line.unwrap();
        for capture in pattern.captures_iter(&line) {
            let d1: i32 = capture[1].parse().unwrap();
            let d2: i32 = capture[2].parse().unwrap();
            result += d1 * d2;
        }
    }
    println!("{}", result);
}
