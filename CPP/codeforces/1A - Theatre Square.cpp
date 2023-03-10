#include<iostream>
using namespace std;

long long fun(auto n, auto a) {
    auto x = n / a;
    auto y = n % a;
    if (y != 0) {
        x += 1;
    }
    return x;
}

int main() {
    long long n, m, a;
    cin >> n >> m >> a;
    auto x = fun(n, a);
    auto y = fun(m, a);
    cout << x * y << endl;

    return 0;
}