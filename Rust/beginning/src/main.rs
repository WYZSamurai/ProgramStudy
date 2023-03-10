use std::io::stdin;
fn main() {
    let mut n = String::new();
    stdin().read_line(&mut n).unwrap();
    let n = n.trim().parse::<i32>().unwrap();

    let mut v: Vec<String> = Vec::new();
    for _i in 0..n {
        let mut s = String::new();
        stdin().read_line(&mut s).unwrap();
        let a = s;
        v.push(a);
    }
}
