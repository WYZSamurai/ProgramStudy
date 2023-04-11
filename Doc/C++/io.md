## const
const默认作用于其左边的东西，否则作用于其右边的东西
## IO
    std::string s;
    // 读入行
    getline(std::cin, s);
## 现代化C++
### 智能指针
### std::string 和 std::string_view
1. char转int：char-'0'
2. int转string：to_string(int)
3. string转int：stoi(string)
****
- c_str ()：返回一个以空字符结尾的C风格字符串（const char *）。
- data ()：返回一个指向当前字符串数据（const char *）的指针。
- length ()：返回字符串的长度，即字符的个数。时间复杂度为O (1)。
- at (index)：返回指定索引处的字符，索引从0开始。时间复杂度为O (1)。
- operator [] (index)：返回指定索引处的字符，索引从0开始。时间复杂度为O (1)。
- append (str)：在字符串末尾添加另一个字符串。时间复杂度为O (n)，其中n是另一个字符串的长度。
- operator += (str)：在字符串末尾添加另一个字符串。时间复杂度为O (n)，其中n是另一个字符串的长度。
- assign (str)：用另一个字符串替换当前字符串的内容。时间复杂度为O (n)，其中n是另一个字符串的长度。
- insert (pos, str)：在指定位置插入另一个字符串。时间复杂度为O (m + n)，其中m是当前字符串的长度，n是另一个字符串的长度。
- erase (pos, len)：删除从指定位置开始的指定长度的子串。时间复杂度为O (m - n)，其中m是当前字符串的长度，n是子串的长度。
- replace (pos, len, str)：用另一个字符串替换从指定位置开始的指定长度的子串。时间复杂度为O (m - n + k)，其中m是当前字符串的长度，n是子串的长度，k是另一个字符串的长度。
- swap (str)：交换当前字符串和另一个字符串的内容。时间复杂度为O (1)。
- substr (pos, len)：返回从指定位置开始的指定长度的子串。时间复杂度为O (n)，其中n是子串的长度。
- compare (str)：按字典顺序比较当前字符串和另一个字符串，返回负数，0或正数，分别表示小于，等于或大于。时间复杂度为O (n)，其中n是两个字符串中较短者的长度。
- find (str, pos)：从指定位置开始查找另一个字符串在当前字符串中第一次出现的位置，如果没有找到，返回string::npos。时间复杂度为O ((m - n + 1) * n)，其中m是当前字符串的长度，n是另一个字符串的长度。
- rfind (str, pos)：从指定位置开始反向查找另一个字符串在当前字符串中最后一次出现的位置，如果没有找到，返回string::npos。时间复杂度为O ((m - n + 1) * n)，其中m是当前字符串的长度，n是另一个字符串的长度。
- find_first_of (str, pos)：从指定位置开始查找当前字符串中第一个属于另一个字符串中的任意字符的位置，如果没有找到，返回string::npos。时间复杂度为O ((m - n + 1) * n)，其中m是当前字符串的长度，n是另一个字符串的长度。
- find_last_of (str, pos)：从指定位置开始反向查找当前字符串中最后一个属于另一个字符串中的任意字符的位置，如果没有找到，返回string::npos。时间复杂度为O ((m - n + 1) * n)，其中m是当前字符串的长度，n是另一个字符串的长度。
- find_first_not_of (str, pos)：从指定位置开始查找当前字符串中第一个不属于另一个字符串中的任意字符的位置，如果没有找到，返回string::npos。时间复杂度为O ((m - n + 1) * n)
### std::vector 和其他标准库容器
#### vector
1. 获取vector中第n个元素：vector.at(n-1)
2. 插入vector第n个位置前：vector.insert(vector.begin()+n-1,val)
****
- size ()：返回vector中元素的个数。
- empty ()：判断vector是否为空，即是否没有元素。
- push_back (x)：在vector的末尾添加一个元素x。
- pop_back ()：删除vector的最后一个元素。
- insert (pos, x)：在pos指定的位置插入一个元素x，pos可以是一个迭代器或一个下标。
- erase (pos)：删除pos指定的位置的元素，pos可以是一个迭代器或一个下标。
- erase (first, last)：删除[first, last)区间内的所有元素，first和last都是迭代器。
- clear ()：清空vector中的所有元素。
- swap (v)：交换当前vector和另一个vector v的内容。
- at (index)：返回指定索引处的元素的引用，索引从0开始。如果索引越界，会抛出异常。
- operator [] (index)：返回指定索引处的元素的引用，索引从0开始。如果索引越界，不会抛出异常，但会导致未定义的行为。
- front ()：返回第一个元素的引用。
- back ()：返回最后一个元素的引用。
- begin ()：返回指向第一个元素的迭代器。
- end ()：返回指向最后一个元素之后的迭代器。
- rbegin ()：返回指向最后一个元素的反向迭代器。
- rend ()：返回指向第一个元素之前的反向迭代器。
- data ()：返回指向容器中第一个元素的指针。
- resize (n)：重新分配容器的大小，使其能容纳n个元素。
- reserve (n)：请求容器改变其容量，使其至少能容纳n个元素。
- shrink_to_fit ()：减少容器的容量，使其与其大小相适应。
****
- size ()：O(1)
- empty ()：O(1)
- push_back (x)：均摊O(1)
- pop_back ()：O(1)
- insert (pos, x)：O(n)，其中n是插入位置之后的元素数。
- erase (pos)：O(n)，其中n是删除位置之后的元素数。
- erase (first, last)：O(n)，其中n是删除区间内的元素数。
- clear ()：O(n)，其中n是容器中的元素数。
- swap (v)：O(1)。
- at (index)：O(1)。
- operator [] (index)：O(1)。
- front ()：O(1)。
- back ()：O(1)。
- begin ()：O(1)。
- end ()：O(1)。
- rbegin ()：O(1)。
- rend ()：O(1)。
- data ()：O(1)。
- resize (n)：O(n)，其中n是新的容器大小。
- reserve (n)：均摊O(n)，其中n是新的容器容量。
- shrink_to_fit ()：均摊O(n)，其中n是容器中的元素数。
#### Map
- size ()：O(1)。
- empty ()：O(1)。
- insert (x)：O(logn)，其中n是容器中的元素数。
- erase (pos)：O(logn)，其中n是容器中的元素数。
- erase (first, last)：O(logn + k)，其中n是容器中的元素数，k是删除区间内的元素数。
- clear ()：O(n)，其中n是容器中的元素数。
- swap (m)：O(1)。
- at (key)：O(logn)，其中n是容器中的元素数。
- operator [] (key)：O(logn)，其中n是容器中的元素数。
- find (key)：O(logn)，其中n是容器中的元素数。
- count (key)：O(logn)，其中n是容器中的元素数。
- lower_bound (key)：O(logn)，其中n是容器中的元素数。
- upper_bound (key)：O(logn)，其中n是容器中的元素数。
- equal_range (key)：O(logn)，其中n是容器中的元素数。
- begin ()：O(1)。
- end ()：O(1)。
- rbegin ()：O(1)。
- rend ()：O(1)。
### 标准库算法
#### for_each
#### transform
#### find_if
#### sort、lower_bound
### 用constexpr替代define
在现代 C++ 中，应优先使用 constexpr 变量定义编译时常量

    #define SIZE 10 // C-style
    constexpr int size = 10; // modern C++
### 统一初始化
    // C++20 新的通用初始化
    int x{ 1 };
    std::vector<S> v2 {s1, s2, s3};
### 移动语义
### Lambda 表达式
### 异常
### std::atomic
### std::variant