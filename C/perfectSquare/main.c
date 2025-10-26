#include <stdio.h>
#include <math.h>

// Quadrado perfeito: n * n
// resultante da multiplicação de um número por ele msm
long int findNextSquare(long int sq);

int main(void) {
    findNextSquare(625);
}
long int findNextSquare(long int sq) {
    long int perfectSquare, nextSquare;
    for (size_t i = 0; i < 12345678; i++) {
        perfectSquare = i * i;
        
        if (perfectSquare == sq) {
            nextSquare = perfectSquare + 2*i + 1;
            return nextSquare;
        }
        
    }
    return -1;
}