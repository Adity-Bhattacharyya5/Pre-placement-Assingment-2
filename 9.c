#include <stdio.h>

int main() {
    int n, i, j, flag = 1;
    printf("Enter size of square matrix: ");
    scanf("%d", &n);

    int mat[n][n];

    printf("Enter matrix elements:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", &mat[i][j]);
        }
    }

    // Check identity matrix
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if ((i == j && mat[i][j] != 1) || (i != j && mat[i][j] != 0)) {
                flag = 0;
                break;
            }
        }
    }

    if (flag)
        printf("The matrix is an Identity Matrix\n");
    else
        printf("The matrix is NOT an Identity Matrix\n");

    return 0;
}
