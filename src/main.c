#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int multiply(int a, int b) {
    return a * b;
}

int main() {
    printf("=== Simple Calculator Program ===\n");
    printf("5 + 3 = %d\n", add(5, 3));
    printf("5 * 3 = %d\n", multiply(5, 3));
    printf("10 + 20 = %d\n", add(10, 20));
    printf("10 * 20 = %d\n", multiply(10, 20));
    printf("================================\n");
    return 0;
}
