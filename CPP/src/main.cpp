#include<iostream>
#include<string>
using namespace std;

constexpr string_view day[]{ "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN" };

int main() {
    string str1;
    string str2;
    string str3;
    string str4;
    cin >> str1;
    cin >> str2;
    cin >> str3;
    cin >> str4;
    auto first{ 0 };
    for (size_t i{ 0 }; i < str1.length(); i++) {
        if (str1[i] == str2[i] && (str1[i] >= 'A' && str1[i] <= 'G')) {
            cout << day[str1[i] - 'A'] << ' ';
            first = i;
            break;
        }
    }

    for (size_t i{ first + 1 }; i < str1.length(); i++) {
        if (str1[i] == str2[i]) {
            if (str1[i] >= '0' && str1[i] <= '9') {
                cout << '0' << str1[i] - '0' << ':';
                break;
            }
            else if (str1[i] >= 'A' && str1[i] <= 'N') {
                cout << str1[i] - 'A' + 10 << ':';
                break;
            }
        }
    }

    for (size_t i{ 0 }; i < str3.length(); i++) {
        if (str3[i] == str4[i] && ((str3[i] >= 'A' && str3[i] <= 'Z') || (str3[i] >= 'a' && str3[i] <= 'z'))) {
            if (i < 10) {
                cout << '0' << i;
            }
            else {
                cout << i;
            }
            break;
        }
    }
}