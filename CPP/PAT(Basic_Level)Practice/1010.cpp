#include <stdio.h>
int main() {
    int i = 0, a[10001], y = 0;
    char ch;
    do scanf("%d%c", &a[i++], &ch); while (ch != '\n');	//输入任意个整数
    for (int j = 0; j < i; j += 2) a[j] *= a[j + 1]--;
    for (int j = 0; j < i; j += 2)
        if (a[j] != 0) j ? printf(" %d %d", a[j], a[j + 1]) : y = printf("%d %d", a[j], a[j + 1]);
    if (y == 0) printf("0 0");	//任何项系数都为0的时候就是零多项式，只输出0 0
    return 0;
}
