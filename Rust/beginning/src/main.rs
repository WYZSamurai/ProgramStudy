fn main() {
    let mut s = String::from("value");
    fun(&mut s);
    println!("{}", s);
}

fn fun(s: &mut String) {
    s.push_str("string");
}
