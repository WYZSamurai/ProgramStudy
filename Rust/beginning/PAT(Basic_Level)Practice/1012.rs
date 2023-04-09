use std::io::stdin;
fn main() {
    let v = iom();
    fun(&v);
}

fn iom() -> Vec<i32> {
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    let mut v: Vec<i32> = Vec::new();
    for i in s.trim().split(' ') {
        v.push(i.to_string().parse().unwrap());
    }
    v
}

fn fun(v: &Vec<i32>) {
    let (mut a1, mut a2, mut a3, mut a4, mut a5) = (0, 0, 0, 0.0, 0);
    let (mut n1, mut n2, mut n3, mut n4, mut n5) = (false, false, false, false, false);
    let mut flag = true;
    let mut cx = 0;
    for i in 1..v.len() {
        if v[i] % 5 == 0 && v[i] % 2 == 0 {
            a1 += v[i];
            n1 = true;
        } else if v[i] % 5 == 1 {
            if flag {
                a2 += v[i];
                flag = false;
                n2 = true;
            } else {
                a2 -= v[i];
                flag = true;
                n2 = true;
            }
        } else if v[i] % 5 == 2 {
            a3 += 1;
            n3 = true;
        } else if v[i] % 5 == 3 {
            a4 += v[i] as f64;
            cx += 1;
            n4 = true;
        } else if v[i] % 5 == 4 {
            n5 = true;
            if v[i] > a5 {
                a5 = v[i];
            }
        }
    }
    if n1 {
        print!("{} ", a1);
    } else {
        print!("N ");
    }
    if n2 {
        print!("{} ", a2);
    } else {
        print!("N ");
    }
    if n3 {
        print!("{} ", a3);
    } else {
        print!("N ");
    }
    if n4 {
        print!("{:.1} ", a4 / cx as f64);
    } else {
        print!("N ");
    }
    if n5 {
        print!("{}", a5);
    } else {
        print!("N");
    }
}
