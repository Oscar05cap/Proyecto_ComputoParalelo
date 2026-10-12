import sys, time
n = int(sys.argv[1]) if len(sys.argv) > 1 else 128
reps = int(sys.argv[2]) if len(sys.argv) > 2 else 5

A = [[(i + n * j) % 7 * 0.5 for j in range(n)] for i in range(n)]
B = [[(i * n + j) % 5 * 0.25 for j in range(n)] for i in range(n)]

def matmul(A, B, n):
    C = [[0.0] * n for _ in range(n)]
    for i in range(n):
        Ai, Ci = A[i], C[i]
        for k in range(n):
            a, Bk = Ai[k], B[k]
            for j in range(n):
                Ci[j] += a * Bk[j]
    return C

matmul(A, B, n)  

for r in range(1, reps + 1):
    t0 = time.perf_counter(); C = matmul(A, B, n); t = time.perf_counter() - t0
    chk = C[0][0] + C[n // 2][n // 2] + C[-1][-1]
    print(f"py_puro,{n},{r},{t:.6f},{2 * n**3 / t / 1e9:.4f},{chk:.6e}")