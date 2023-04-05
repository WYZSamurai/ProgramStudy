#include<iostream>
using namespace std;

uint16_t fun(uint16_t& x) {
    if (x % 2 == 0) {
        x = x / 2;
    }
    else {
        x = (3 * x + 1) / 2;
    }
    return x;
}

int main() {
    uint16_t x;
    cin >> x;
    uint16_t cx = 0;
    while (x != 1) {
        x = fun(x);
        cx += 1;
    }
    cout << cx << endl;
}