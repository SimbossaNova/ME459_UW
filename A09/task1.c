#include "matmul.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char* argv[]) {
  if (argc != 2) {
    printf("Usage: ./task1 n\n");
    return 1;
  }

  int n = atoi(argv[1]);
  if (n <= 0) {
    printf("n must be greater than zero\n");
    return 1;
  }

  double* A = (double*)malloc(n * n * sizeof(double));
  double* B = (double*)malloc(n * n * sizeof(double));
  double* C = (double*)malloc(n * n * sizeof(double));

  if (A == NULL || B == NULL || C == NULL) {
    printf("Memory allocation failed\n");
    return 1;
  }

  for (int i = 0; i < n * n; ++i) {
    A[i] = ((double)rand() / RAND_MAX) * 2 - 1;
    B[i] = ((double)rand() / RAND_MAX) * 2 - 1;
  }

  clock_t start = clock();
  mmul1(A, B, C, n);
  clock_t end = clock();
  double time_mmul1 = ((double)end - start) / CLOCKS_PER_SEC * 1000.0;

  printf("Time taken by mmul1: %.1f ms\n", time_mmul1);
  printf("Last element of matrix C: %.1f\n", C[n * n - 1]);

  
  free(A);
  free(B);
  free(C);

  return 0;
}
