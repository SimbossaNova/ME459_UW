#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "matmul.h"

double get_random_double() {
    return ((double)rand() / (double)RAND_MAX) * 2.0 - 1.0;
}

int main() {
    srand(time(0));

    const size_t n = 1024;

    double* A = (double*)malloc(n * n * sizeof(double));
    double* B = (double*)malloc(n * n * sizeof(double));
    double* C = (double*)malloc(n * n * sizeof(double));

    double* B_rowcol = (double*)malloc(n * n * sizeof(double));




    for (size_t i = 0; i < n * n; i++) {
        A[i] = get_random_double();
        B[i] = get_random_double();
    }

    clock_t start = clock();
    mmul1(A, B, C, n);
    clock_t end = clock();
    double time_mmul1 = ((double)end - start) / CLOCKS_PER_SEC * 1000.0;

    printf("t1 %.2f ms\n%.2f\n", time_mmul1, C[n * n - 1]);

    start = clock();
    mmul2(A, B, C, n);
    end = clock();
    double time_mmul2 = ((double)end - start) / CLOCKS_PER_SEC * 1000.0;

    printf("t2 %.2f ms\n%.2f\n", time_mmul2, C[n * n - 1]);


    for (int i = 0; i < 1024; i++) {
        for (int j = 0; j < 1024; j++) {
            B_rowcol[j * 1024 + i] = B[i * 1024 + j];
        }
    }
    start = clock();
    mmul3(A, B_rowcol, C, n);
    end = clock();
    double time_mmul3 = ((double)end - start) / CLOCKS_PER_SEC * 1000.0;

    printf("t3 %.2f ms\n%.2f\n", time_mmul3, C[n * n - 1]);


    start = clock();
    mmul4(A, B_rowcol, C, n);
    end = clock();
    double time_mmul4 = ((double)end - start) / CLOCKS_PER_SEC * 1000.0;

    printf("t4 %.2f ms\n%.2f\n", time_mmul4, C[n * n - 1]);

    free(A);
    free(B);
    free(C);

    return 0;
}