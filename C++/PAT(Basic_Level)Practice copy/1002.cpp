/*
1.char转int：char-'0'
2.int转string：to_string(int)
3.string转int：stoi(string)
*/
#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main() {
    vector<string> list = { "ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu" };
    string s;
    cin >> s;
    int32_t sum = 0;
    for (auto& i : s) {
        sum += i - '0';
    }
    string res = to_string(sum);
    string s2 = "";
    for (auto& i : res) {
        int32_t a = i - '0';
        if (s2 == "") {
            s2 += list[a];
        }
        else {
            s2 += " ";
            s2 += list[a];
        }
    }
    cout << s2 << endl;

}