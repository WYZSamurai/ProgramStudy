fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        None => None,
        Some(x) => Some(x + 1),
    }
}

fn main() {
    let a = Some(21);
    let b = plus_one(a);
    let none = plus_one(None);
    println!("{:#?}", a);
    println!("{:#?}", b);
    println!("{:#?}", none);
}
