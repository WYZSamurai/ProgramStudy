#[derive(Debug)]
enum Province {
    Shaanxi,
    Heibei,
    Shanghai,
}
enum Coin {
    Shiyuan,
    Wuyuan,
    Yiyuan(Province),
}

fn main() {
    let c = Coin::Shiyuan;
    match c {
        Coin::Shiyuan => println!("{}", 10),
        Coin::Wuyuan => {
            let a = 5;
            println!("{}", a);
        }
        Coin::Yiyuan(province) => println!("{:#?}", province),
    }
}
