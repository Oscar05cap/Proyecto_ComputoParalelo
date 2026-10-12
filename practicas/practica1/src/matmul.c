// matmul.c - linea base secuencial (i-j-k) para C = A·B con matrices n x n de double
// Uso: ./matmul <n> <repeticiones> <etiqueta>
// Salida CSV: etiqueta,n,rep,segundos,gflops,checksum
#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

static double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec * 1e-9;
}

static void matmul(int n, const double *A, const double *B, double *C) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            double s = 0.0;
            for (int k = 0; k < n; k++)
                s += A[i * n + k] * B[k * n + j];
            C[i * n + j] = s;
        }
}

int main(int argc, char **argv) {
    int n    = argc > 1 ? atoi(argv[1]) : 512;
    int reps = argc > 2 ? atoi(argv[2]) : 5;
    const char *tag = argc > 3 ? argv[3] : "c";

    double *A = malloc(sizeof(double) * n * n);
    double *B = malloc(sizeof(double) * n * n);
    double *C = malloc(sizeof(double) * n * n);

    for (int i = 0; i < n * n; i++) {
        A[i] = (i % 7) * 0.5;
        B[i] = (i % 5) * 0.25;
    }

    matmul(n, A, B, C);  /* calentamiento: no se reporta */

    for (int r = 1; r <= reps; r++) {
        double t0 = now();
        matmul(n, A, B, C);
        double t = now() - t0;
        double gflops = 2.0 * n * n * n / t / 1e9;
        double checksum = C[0] + C[(n * n) / 2] + C[n * n - 1];
        printf("%s,%d,%d,%.6f,%.3f,%.6e\n", tag, n, r, t, gflops, checksum);
    }

    free(A); free(B); free(C);
    return 0;
}