#include <stdio.h>
#define TURE 1
#define FALSE 0

int fun(int n) {
    int res = TURE;
    for (int i = n - 1;i > 1;i--) {
        if (n % i == 0) {
            res = FALSE;
        }
    }
    return res;
}

int main(void) {

    // 输入正整数
    int n;
    scanf("%d", &n);
    // for (int i = 1;i <= n;i++) {
    //     if (fun(i)) {
    //         printf("%d\n", i);
    //     }
    // }
    // 定义计数变量
    int cx = 0;
    int dx = 0;
    for (int i = 1;i <= n;i++) {
        // 如果是第一个素数则存入dx
        if (fun(i) == TURE && dx == 0) {
            dx = i;
        }
        // 如果是素数则与dx相减,若结果为二则将结果录入dx，cx+1，i+2
        else if (fun(i) == TURE) {
            if (i - dx == 2) {
                dx = i;
                cx += 1;
                // i += 2;
            }
        }
    }
    printf("%d\n", cx);

    return 0;
}