#include <stdio.h> 
#include <stdbool.h>
#include <string.h> // strlen
#include <ctype.h> // tolower

bool IsIsogram (const char *string);

int main(void) {
    IsIsogram("AbBcDEff");
}
bool IsIsogram (const char *string) {
    size_t length = strlen(string); // Tamanho da str
    bool isIsogram = true;
    char lowerString[length]; // String em lowercase
    char stringChars[length]; // caracteres já presentes
    for (size_t i = 0; i < length; i++) {
        lowerString[i] = tolower(string[i]);
        stringChars[i] = lowerString[i];
        for (size_t j = 0; j < i; j++) {
            // Percorre a array stringChars
            if (lowerString[i] == stringChars[j]) {
                printf("Repetição no caractere '%c'\n", lowerString[i]);
                isIsogram = false;
            }
        }
    }
    return isIsogram;
}