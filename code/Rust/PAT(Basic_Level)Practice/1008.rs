use std::io::stdin;
fn main() {
    let (m, mut tmp) = iom();
    fun(&m, &mut tmp);
    for i in 0..tmp.len() {
        if i == tmp.len() - 1 {
            print!("{}", tmp[i]);
        } else {
            print!("{} ", tmp[i]);
        }
    }
}
fn fun(n: &i32, tmp: &mut Vec<i32>) {
    for _i in 0..*n {
        let a = *tmp.last().unwrap();
        tmp.pop();
        tmp.insert(0, a);
    }
}

fn iom() -> (i32, Vec<i32>) {
    let mut s = String::new();
    let (_n, m): (i32, i32);

    stdin().read_line(&mut s).unwrap();
    let mut tmp: Vec<i32> = Vec::new();
    for i in s.trim().split(" ") {
        tmp.push(i.to_string().parse().unwrap());
    }
    _n = tmp[0];
    m = tmp[1];

    tmp.clear();
    s.clear();

    stdin().read_line(&mut s).unwrap();
    for i in s.trim().split(" ") {
        tmp.push(i.to_string().parse().unwrap());
    }
    (m, tmp)
}
