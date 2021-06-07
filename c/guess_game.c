#include <stdio.h>

int main() {
    int hidden = 12;
    int guess = 0;
    int guesscount = 0;
    int guesslimit = 3;
    int outofguesses = 0;

    while (guess != hidden && outofguesses == 0) {
        if (guesscount < guesslimit) {
            printf("Enter ur number: ");
            scanf("%d", &guess);
            guesscount++;
        } else {
            outofguesses = 1;
        }
    }

    if (outofguesses == 1) {
        printf("yeah out of guesses wtf");
    } else {
        printf("you won uh ye");
    }
}
