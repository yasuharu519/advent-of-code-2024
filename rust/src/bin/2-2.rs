use std::io;

fn main() {
    let stdin = io::stdin();
    let lines = stdin.lines();

    fn check(nums: &Vec<i64>) -> bool {
        let diff = nums[1] - nums[0];
        if diff >= 0 {
            nums.windows(2)
                .all(|w| w[1] - w[0] >= 1 && w[1] - w[0] <= 3)
        } else {
            nums.windows(2)
                .all(|w| w[1] - w[0] >= -3 && w[1] - w[0] <= -1)
        }
    }

    let mut result: i64 = 0;
    for line in lines {
        let nums: Vec<i64> = line
            .unwrap()
            .split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();
        if check(&nums) {
            result += 1;
            continue;
        }

        for i in 0..nums.len() {
            let nums = nums[..i]
                .iter()
                .chain(nums[i + 1..].iter())
                .cloned()
                .collect();
            if check(&nums) {
                result += 1;
                break;
            }
        }
    }

    println!("{}", result);
}
