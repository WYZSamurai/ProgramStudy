use std::io::stdin;

fn main() {
    let vec = iom();
    let len = vec.len();
    for i in 0..len {
        if fun(&vec[i][0], &vec[i][1], &vec[i][2]) {
            println!("Case #{}: true", i + 1);
        } else {
            println!("Case #{}: false", i + 1);
        }
    }
}
fn iom() -> Vec<Vec<i64>> {
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    let n = s.trim().parse::<i64>().unwrap();
    let mut vec: Vec<Vec<i64>> = Vec::new();
    for _i in 0..n {
        let mut tmp: Vec<i64> = Vec::new();
        s.clear();
        stdin().read_line(&mut s).unwrap();
        for i in s.trim().split(" ") {
            tmp.push(i.to_string().parse().unwrap());
        }
        vec.push(tmp);
    }
    vec
}

fn fun(a: &i64, b: &i64, c: &i64) -> bool {
    if *a + *b > *c {
        true
    } else {
        false
    }
}
