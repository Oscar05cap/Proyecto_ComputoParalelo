import sys, time
import numpy as np

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1024
reps = int(sys.argv[2]) if len(sys.argv) > 2 else 5

rng = np.random.default_rng(0)               
A = rng.random((n, n)); B = rng.random((n, n))

C = A @ B                                      

for r in range(1, reps + 1):
    c0 = time.process_time(); t0 = time.perf_counter()
    C = A @ B
    t = time.perf_counter() - t0
    c = time.process_time() - c0
    print(f"numpy,{n},{r},{t:.6f},{2 * n**3 / t / 1e9:.3f},{c / t:.2f}")