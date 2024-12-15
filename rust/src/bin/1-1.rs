use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io;

fn main() {
    let stdin = io::stdin();
    let lines = stdin.lines();

    let mut left = BinaryHeap::new();
    let mut right = BinaryHeap::new();

    for line in lines {
        let line = line.unwrap();
        if line.trim().is_empty() {
            continue;
        }

        let [a, b]: [i64; 2] = line
            .split_whitespace()
            .map(|x| x.parse::<i64>().unwrap())
            .collect::<Vec<_>>()
            .try_into()
            .unwrap();

        left.push(Reverse(a));
        right.push(Reverse(b));
    }

    let mut result: i64 = 0;
    while let (Some(Reverse(a)), Some(Reverse(b))) = (left.pop(), right.pop()) {
        result += (a - b).abs();
    }

    println!("{}", result);
}
