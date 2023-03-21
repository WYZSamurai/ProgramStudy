struct Man {
    name: String,
    age: i8,
}
impl Man {
    fn new(name: String, age: i8) -> Self {
        Self { name, age }
    }
}

enum Item {
    Apple { kg: i8, price: i8 },
    Peach(i32),
    Watermelon,
}

fn main() {
    let d = String::from("Yizhen");
    let m1 = Man::new(d, 12);
    println!("{} {}", m1.name, m1.age);
    let i1 = Item::Apple {
        kg: (12),
        price: (30),
    };
    let i2 = Item::Peach(2);
    let i3 = Item::Watermelon;
}
