#include <stdio.h>

int main(int argc, char *argv[]){
    int i,j,k,n, count=0;
    int *mas;
    char *filename = argv[1];
    FILE *fp;

    if ((fp = fopen(filename, "r")) == NULL) {
        printf("Can't open file %s\n", filename);
    }

    fscanf(fp, "%d\n", &n);

    if ((mas = (int *) calloc(n, sizeof(int))) == NULL){
        printf("Can't allocate memory");
    }

    for (i = 0; i < n; i++){
        fscanf(fp, "%d", mas+i);
    }

    for (i = 0; i < n - 2; i++){
        for (j = i+1; j< n - 1; j++){
            for (k = j+1; k < n; k++){
                if ((mas[i] + mas[j] + mas[k]) == 0) {
                    count++;
                }
            }
        }
    }
    printf("%d\n", count);

    return 0;
}