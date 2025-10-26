#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool is_square(int n);

int main(void) {
    printf("%b", is_square(4));
}

// bool is_square(int n) {
//     for (int i = 0; i <= 12345678; i++) {
//         if (i * i == n) {
//             return true;
//         } 
//     }
//     return false;
// }
// Correção:
bool is_square(int n) {
    int square = sqrt(n);
    return n == square * square;
}