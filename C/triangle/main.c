#include <stdio.h>
#include <stdbool.h>

bool is_triangle(int a, int b, int c);
int main(void) {
    printf("%b", is_triangle(1, 2, 2));
}
bool is_triangle(int a, int b, int c) {
    return a + b > c && a + c > b && b + c > a;
}