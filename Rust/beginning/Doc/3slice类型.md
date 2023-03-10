### slice类型
> slice 允许你引用集合中一段连续的元素序列，而不用引用整个集合。slice 是一类引用，所以它没有所有权。  
#### 字符串slice(&str)

    fn main() {
        let mut s = String::from("hello world");

        let s1 = &s[..5];//s1->&str取前5个元素
        let s2 = &s[6..];//s2->&str取第六个之后的元素
        let s3 = &s[..];//s3->&str取整个元素
        println!("{s1} {s2}");
        println!("{s3}");

        let s4 = fun(&s);
        s.clear();
        println!("{s4}");
    }

    fn fun(s: &String) -> &str {
        let bytes = s.as_bytes();
        for (i, &item) in bytes.iter().enumerate() {
            if item == b' ' {//当找到空格后返回之前的元素
                return &s[0..i];
            }
        }
        &s//否则返回整段元素
    }  
字符串常量就是一个Slice类型（&str）（不可变引用）

    let s = "hello world";
进一步改进，将s的参数类型改为&str，既能对整个字符串操作，又能对一部分切片操作

    fn first_word(s: &str) -> &str {
        let bytes = s.as_bytes();

        for (i, &item) in bytes.iter().enumerate() {
            if item == b' ' {
                return &s[0..i];
            }
        }

        &s[..]
    }

    fn main() {
        let my_string = String::from("hello world");

        // `first_word` 适用于 `String`（的 slice），整体或全部
        let word = first_word(&my_string[0..6]);
        let word = first_word(&my_string[..]);
        // `first_word` 也适用于 `String` 的引用，
        // 这等价于整个 `String` 的 slice
        let word = first_word(&my_string);

        let my_string_literal = "hello world";

        // `first_word` 适用于字符串字面值，整体或全部
        let word = first_word(&my_string_literal[0..6]);
        let word = first_word(&my_string_literal[..]);

        // 因为字符串字面值已经是字符串 slice 了，
        // 这也是适用的，无需 slice 语法！
        let word = first_word(my_string_literal);
    }
#### 其他类型slice

    let a = [1, 2, 3, 4, 5];
    for i in &a[..4] {//遍历一部分数组
        println!("{i}");
    }
    let slice = &a[1..3];//&[i32]->&[2,3]
    assert_eq!(slice, &[2, 3]);