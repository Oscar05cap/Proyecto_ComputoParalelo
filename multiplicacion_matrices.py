import os
os.environ["OMP_NUM_THREADS"]      = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"]      = "1"

import numpy as np, time

def bench(N, dtype=np.float32, reps=5):
    A = np.random.rand(N, N).astype(dtype)
    B = np.random.rand(N, N).astype(dtype)
    C = A @ B
    t0 = time.perf_counter()
    for _ in range(reps):
        C = A @ B
    dt = (time.perf_counter() - t0) / reps
    gflops = 2 * N**3 / dt / 1e9
    print(f"N={N:5d}  dtype={np.dtype(dtype).name:8s}  "
          f"t={dt*1000:8.2f} ms  {gflops:7.2f} GFLOPS")

if __name__ == "__main__":
    print("Backend:", np.__config__.show() or "")
    for N in (256, 512, 1024, 2048, 4096):
        bench(N, np.float32)
        bench(N, np.float64)