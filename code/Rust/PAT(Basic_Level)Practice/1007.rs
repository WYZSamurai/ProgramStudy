use std::io::stdin;
fn main() {
    let x = iom();
    let res = f1007(&x);
    print!("{}", res);
}

fn iom() -> u32 {
    let mut n: String = String::new();
    stdin().read_line(&mut n).unwrap();
    let n: u32 = n.trim().parse().unwrap();
    n
}

fn is_prime(n: &u32) -> bool {
    if *n <= 1 {
        return false;
    }
    if *n % 2 == 0 && *n != 2 {
        return false;
    }
    for i in (3..=(*n as f32).sqrt() as u32).step_by(2) {
        if *n % i == 0 {
            return false;
        }
    }
    true
}

fn f1007(x: &u32) -> u32 {
    let mut dx: u32 = 3;
    let mut cx: u32 = 0;
    for i in (3..*x + 1).step_by(2) {
        if is_prime(&i) && i - 2 == dx && is_prime(&dx) {
            cx += 1;
        }
        dx = i;
    }
    cx
}
