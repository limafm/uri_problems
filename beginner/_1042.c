#include <stdio.h>
 
int main() {
 
    int a,b,c;

    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
 
    int vet2 [] = {a,b,c};
    int vet1[3];
    int i;

    if ((a > b) && (a > c)) {
        if (b > c) {
            vet1[2] = a; vet1[1] = b; vet1[0] = c;
        }
        else {
            vet1[2] = a; vet1[1] = c; vet1[0] = b;
        }
    }

    else if ((b > a) && (b > c)) {
        if (a > c) {
            vet1[2] = b; vet1[1] = a; vet1[0] = c;
        }
        else {
            vet1[2] = b; vet1[1] = c; vet1[0] = a;
        }
    }

    if ((c > b) && (c > a)) {
        if (b > a) {
            vet1[2] = c; vet1[1] = b; vet1[0] = a;
        }
        else {
            vet1[2] = c; vet1[1] = a; vet1[0] = b;
        }
    }

    for (i=0; i<3; i++) {
        printf("%d\n", vet1[i]);
    }
    printf("\n");
    for (i=0; i<3; i++) {
        printf("%d\n", vet2[i]);
    }

    return 0;
}