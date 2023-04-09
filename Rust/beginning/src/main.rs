use std::io::stdin;
fn main() {
    let vec = iom();
    let mut res: Vec<i32> = Vec::new();
    let mut tp = 0;
    for i in 0..vec.len() {
        if i % 2 == 0 {
            tp = vec[i];
        } else {
            let x = tp * vec[i];
            if x != 0 {
                res.push(x);
                res.push(vec[i] - 1)
            } else if x == 0 && i == 1 {
                res.push(0);
                res.push(0);
                break;
            }
        }
    }
    for i in 0..res.len() {
        if i == res.len() - 1 {
            print!("{}", res[i]);
        } else {
            print!("{} ", res[i]);
        }
    }
}

fn iom() -> Vec<i32> {
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    let mut vec: Vec<i32> = Vec::new();
    for i in s.trim().split(" ") {
        vec.push(i.to_string().parse().unwrap());
    }
    vec
}
