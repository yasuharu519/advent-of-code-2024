use regex::Regex;
use std::io;

fn main() {
    let pattern = Regex::new(r"(mul)\((\d{1,3}),(\d{1,3})\)|(?:do|don't)\(\)").unwrap();
    let stdin = io::stdin();
    let mut result = 0;
    let mut enabled = true;

    for line in stdin.lines() {
        let line = line.unwrap();

        for capture in pattern.captures_iter(&line) {
            println!("{:?}", capture.get(0).unwrap().as_str());

            if let Some(mul_str) = capture.get(1) {
                if mul_str.as_str() == "mul" {
                    let d1: i32 = capture[2].parse().unwrap();
                    let d2: i32 = capture[3].parse().unwrap();
                    if enabled {
                        result += d1 * d2;
                    }
                }
            } else {
                let matched = capture.get(0).unwrap().as_str();
                if matched == "do()" {
                    enabled = true;
                } else {
                    enabled = false;
                }
            }
        }
    }
    println!("{}", result);
}
