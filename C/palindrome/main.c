#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

bool is_palindrome(const char *str_in);

int main(void) {
    printf("\n%d\n", is_palindrome("a"));
}

bool is_palindrome(const char *str_in) {
    size_t length = strlen(str_in);
    char reversed[length + 1], buffer[length + 1];
    reversed[length] = '\0';
    buffer[length] = '\0';
    for (size_t i = 0; i < length; i++) { 
        // Percorre a entrada do último ao primeiro caracter
        buffer[i] = tolower(str_in[i]); 
        reversed[i] = tolower(str_in[length - 1 - i]);
        // reversed[i] = buffer[i];
        // Coloca o último caracter da entrada no primeiro indice de reversed e... 
    }
    return strcmp(buffer, reversed) == 0;
}