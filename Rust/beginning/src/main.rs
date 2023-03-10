fn main() {
    let s = String::from("abcdefghijk");
    let s1 = s.as_bytes();
    for (i, &item) in s1.iter().enumerate() {
        print!("{},{}\n", i, item as char);
    }
}
