use std::io::*;
fn main() {
    let list = [
        "ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu",
    ];
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    let mut sum = 0;
    let mut s1 = String::new();
    for i in s.trim().split(' ') {
        s1 = i.to_string();
    }
    if s1.len() != 0 {
        for i in s1.chars() {
            sum += i.to_string().parse::<i32>().unwrap();
        }
        s = sum.to_string();
        let len = s.len();
        let s1 = &s[len - 1..];
        let s = &s[..len - 1];
        for i in s.chars() {
            let x = i.to_string().parse::<usize>().unwrap();
            print!("{} ", list[x]);
        }
        for i in s1.chars() {
            let x = i.to_string().parse::<usize>().unwrap();
            println!("{}", list[x]);
        }
    }
}
