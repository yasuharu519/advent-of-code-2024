use std::io;

fn main() {
    let stdin = io::stdin();
    let lines: Vec<Vec<char>> = stdin
        .lines()
        .filter_map(|l| l.ok())
        .map(|l| l.trim().chars().collect())
        .collect();

    fn search(lines: &Vec<Vec<char>>, i: usize, j: usize) -> bool {
        let indices = [(-1, -1), (-1, 1), (1, 1), (1, -1)];
        let pairs = [((0, 1), (2, 3)), ((0, 3), (1, 2))];

        for (l, r) in pairs.iter() {
            let (l1, l2) = *l;
            let (r1, r2) = *r;

            let (l1x, l1y) = (
                (i as isize + indices[l1].0) as usize,
                (j as isize + indices[l1].1) as usize,
            );
            let (l2x, l2y) = (
                (i as isize + indices[l2].0) as usize,
                (j as isize + indices[l2].1) as usize,
            );
            let (r1x, r1y) = (
                (i as isize + indices[r1].0) as usize,
                (j as isize + indices[r1].1) as usize,
            );
            let (r2x, r2y) = (
                (i as isize + indices[r2].0) as usize,
                (j as isize + indices[r2].1) as usize,
            );

            if lines[l1x][l1y] == 'M'
                && lines[l2x][l2y] == 'M'
                && lines[r1x][r1y] == 'S'
                && lines[r2x][r2y] == 'S'
            {
                return true;
            }
            if lines[l1x][l1y] == 'S'
                && lines[l2x][l2y] == 'S'
                && lines[r1x][r1y] == 'M'
                && lines[r2x][r2y] == 'M'
            {
                return true;
            }
        }
        false
    }

    let mut result = 0;

    for i in 1..(lines.len() - 1) {
        for j in 1..(lines[i].len() - 1) {
            if lines[i][j] == 'A' {
                if search(&lines, i, j) {
                    result += 1;
                }
            }
        }
    }

    println!("{}", result);
}
