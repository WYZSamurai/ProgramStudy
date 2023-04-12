use std::io::stdin;
fn main() {
    let v = iom();
    println!("{:?}", v);
}

fn iom() -> Vec<String> {
    let mut v: Vec<String> = Vec::new();
    for _i in 0..4 {
        let mut s = String::new();
        stdin().read_line(&mut s).unwrap();
        v.push(s.trim().to_string());
    }
    v
}
