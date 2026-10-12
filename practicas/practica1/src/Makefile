CC = gcc
CFLAGS_COMMON = -std=c11 -Wall -Wextra

all: matmul_00 matmul_02 matmul_03 hello_omp

matmul_00: matmul.c ; $(CC) -O0 $(CFLAGS_COMMON) $< -o $@
matmul_02: matmul.c ; $(CC) -O2 $(CFLAGS_COMMON) $< -o $@
matmul_03: matmul.c ; $(CC) -O3 -march=native $(CFLAGS_COMMON) $< -o $@
hello_omp: hello_omp.c ; $(CC) -fopenmp $(CFLAGS_COMMON) $< -o $@

clean: ; rm -f matmul_00 matmul_02 matmul_03 hello_omp