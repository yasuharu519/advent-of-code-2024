use std::io;

fn main() {
    let stdin = io::stdin();
    let lines: Vec<String> = stdin
        .lines()
        .filter_map(|l| l.ok())
        .map(|l| l.trim().to_string())
        .collect();

    let grid: Vec<Vec<char>> = lines.iter().map(|line| line.chars().collect()).collect();

    fn search(grid: &Vec<Vec<char>>, i: usize, j: usize) -> i32 {
        let directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ];
        let pattern = ['M', 'A', 'S'];
        let mut count = 0;

        for &(dx, dy) in &directions {
            let mut x = i as isize + dx;
            let mut y = j as isize + dy;
            let mut matched = true;
            for &c in &pattern {
                if x < 0
                    || y < 0
                    || x as usize >= grid.len()
                    || y as usize >= grid[x as usize].len()
                {
                    matched = false;
                    break;
                }
                if grid[x as usize][y as usize] == c {
                    x += dx;
                    y += dy;
                } else {
                    matched = false;
                    break;
                }
            }
            if matched {
                count += 1;
            }
        }

        count
    }

    let mut result = 0;
    for i in 0..grid.len() {
        for j in 0..grid[i].len() {
            if grid[i][j] == 'X' {
                result += search(&grid, i, j);
            }
        }
    }

    println!("{}", result);
}
