use std::io::stdin;

fn func(f: f64, n: f64, h: f64) -> f64 {
    let w = (150.0 / f) * ((n + 1.0) / 2.0).powf(-0.5);
    println!("{}", h);
    return w;
}

fn main() {
    let mut v: Vec<f64> = Vec::new();
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    for i in s.trim().split(" ") {
        v.push(i.to_string().parse().unwrap())
    }
    let (f, n, h) = (v[0], v[1], v[2]);
    println!("{}", func(f, n, h));
}
