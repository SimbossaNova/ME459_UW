
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "sumArray.h"

double* createRandomMatrix(const size_t n);
double measureTime(double (*func)(const double*, const size_t), const double* A, const size_t n);

int main(int argc, char* argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <n>\n", argv[0]);
        return 1;
    }

    const size_t n = atoi(argv[1]);
    if (n < 1 || n > 4096) {
        fprintf(stderr, "n must be between 1 and 4096\n");
        return 1;
    }

    double* A = createRandomMatrix(n);

    double t1 = measureTime(sumArray1, A, n);
    double sum1 = sumArray1(A, n);

    double t2 = measureTime(sumArray2, A, n);
    double sum2 = sumArray2(A, n);

    printf("t1 %.2f ms\n%.2f\n", t2, sum2);
    printf("t2 %.2f ms\n%.2f\n", t2, sum2);

    free(A);

    return 0;
}

double* createRandomMatrix(const size_t n) {
    double* A = malloc(n * n * sizeof(double));

    srand(time(NULL));
    for (size_t i = 0; i < n * n; i++) {
        A[i] = (double)rand() / RAND_MAX * 2.0 - 1.0;
    }

    return A;
}

double measureTime(double (*func)(const double*, const size_t), const double* A, const size_t n) {
    const clock_t start = clock();

    func(A, n);

    const clock_t end = clock();
    const double elapsed = (double)(end - start) / CLOCKS_PER_SEC * 1000.0;

    return elapsed;
}

