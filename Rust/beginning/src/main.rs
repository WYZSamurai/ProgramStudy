fn main() {
    let i = Some(14);
    let s = Some("Stddeijring");
    let c = Some('d');
    let a: Option<i32> = None;
    let x = 5;
    //不能用i32与Option<i32>相加
    //println!("{}", i + x);
    println!("{}", x);
}
