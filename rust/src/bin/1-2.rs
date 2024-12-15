use std::collections::HashMap;
use std::io;

fn main() {
    let stdin = io::stdin();
    let lines = stdin.lines();

    let mut left = HashMap::new();
    let mut right = HashMap::new();

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

        *left.entry(a).or_insert(0) += 1;
        *right.entry(b).or_insert(0) += 1;
    }

    let mut result: i64 = 0;
    left.keys().for_each(|&k| {
        let a = left.get(&k).unwrap_or(&0);
        let b = right.get(&k).unwrap_or(&0);
        result += k * a * b;
    });

    println!("{}", result);
}
