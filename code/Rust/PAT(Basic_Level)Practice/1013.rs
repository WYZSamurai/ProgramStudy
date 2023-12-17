use std::io::stdin;

fn main() {
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    let mut v: Vec<i32> = Vec::new();
    for i in s.trim().split(" ") {
        v.push(i.to_string().parse().unwrap());
    }
    let (n, m) = (*v.get(0).unwrap(), *v.get(1).unwrap());
    fun(n, m);
}

fn fun(n: i32, m: i32) {
    let (mut c1, mut c2) = (0, 0);
    let mut x = 1;
    while c1 < m {
        if is_prime(&x) {
            c1 += 1;
            if c1 >= n {
                c2 += 1;
                if c1 == m {
                    print!("{}", x);
                } else if c2 % 10 != 0 {
                    print!("{} ", x);
                } else {
                    println!("{}", x);
                }
            }
        }
        x += 1;
    }
}

fn is_prime(n: &i32) -> bool {
    if *n <= 1 {
        return false;
    }
    if *n % 2 == 0 && *n != 2 {
        return false;
    }
    for i in (3..=(*n as f32).sqrt() as i32).step_by(2) {
        if *n % i == 0 {
            return false;
        }
    }
    true
}
