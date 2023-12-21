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
    printf("n must be a positive integer\n");
    return 1;
  }

  // Allocate memory for matrices A, B, and C
  double* A = (double*)malloc(n * n * sizeof(double));
  double* B = (double*)malloc(n * n * sizeof(double));
  double* C = (double*)malloc(n * n * sizeof(double));

  // Check if memory allocation is successful
  if (A == NULL || B == NULL || C == NULL) {
    printf("Memory allocation failed\n");
    return 1;
  }

  // Fill matrices A and B with random double values in the range [-1, 1]
  for (int i = 0; i < n * n; ++i) {
    A[i] = ((double)rand() / RAND_MAX) * 2 - 1;
    B[i] = ((double)rand() / RAND_MAX) * 2 - 1;
  }

  // Call mmul1 and measure the time taken
  clock_t start = clock();
  mmul1(A, B, C, n);
  clock_t end = clock();
  double time_mmul1 = ((double)end - start) / CLOCKS_PER_SEC * 1000.0;

  // Output timing results and the last element of matrix C
  printf("Time taken by mmul1: %.1f ms\n", time_mmul1);
  printf("Last element of matrix C: %.1f\n", C[n * n - 1]);

  // Free memory
  
  free(A);
  free(B);
  free(C);

  return 0;
}
