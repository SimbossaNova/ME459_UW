#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void test_1(double* data, int elems, int stride) {
    int i;
    double result = 0.0;
    volatile double sink;
    for (i = 0; i < elems; i += stride) {
        result += data[i];
    }
    sink = result;
}

void test_2(double* data, int elems, int stride) {
    int i;
    volatile double result = 0.0;
    volatile double sink;
    for (i = 0; i < elems; i += stride) {
        result += data[i];
    }
    sink = result;
}

int main() {
    size_t double_size = sizeof(double);
    size_t elems = (1024 * 512) / double_size;
    double* data = (double*)malloc(double_size * elems);
    for (int i = 0; i < (int)elems; i++) {
        data[i] = ((double)rand() / RAND_MAX) * 2.0 - 1.0;
    }
    int stride[] = { 1, 2, 4, 8, 11, 15, 17 };
    int total = sizeof(stride) / sizeof(int);
    double time_hold;
    double average;

    test_1(data, (int)elems, 1);
    for (int i = 0; i < total; i++) {
        time_hold = 0.0;
        average = 0.0;
        for (int j = 0; j < 100; j++) {
            clock_t time = clock();
            test_1(data, (int)elems, stride[i]);
            time = clock() - time;
            double timer = ((double)time) / CLOCKS_PER_SEC * 1000.0;
            time_hold += timer;
        }
        average = time_hold / 100;
        printf("%lf ", average);
    }
    printf("\n");

    test_2(data, (int)elems, 1);
    for (int i = 0; i < total; i++) {
        time_hold = 0.0;
        average = 0.0;
        for (int j = 0; j < 100; j++) {
            clock_t time = clock();
            test_2(data, (int)elems, stride[i]);
            time = clock() - time;
            double timer = ((double)time) / CLOCKS_PER_SEC * 1000.0;
            time_hold += timer;
        }
        average = time_hold / 100;
        printf("%lf ", average);
    }
    printf("\n");

    free(data);
    return 0;
}
