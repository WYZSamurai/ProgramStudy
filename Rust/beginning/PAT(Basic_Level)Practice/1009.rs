use std::io::stdin;
fn main() {
    let mut s = iom();
    fun(&mut s);
}
fn fun(s: &mut String) {
    let mut tmp: Vec<&str> = s.split(" ").collect();
    let len = tmp.len();
    for i in 0..len / 2 {
        tmp.swap(i, len - 1 - i);
    }
    for i in 0..len {
        if i == len - 1 {
            print!("{}", tmp.get(i).unwrap());
            continue;
        }
        print!("{} ", tmp.get(i).unwrap());
    }
}
fn iom() -> String {
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    s.trim().to_string()
}
