#!/usr/bin/env python3
"""Python vs Rust kernel benchmark."""

from __future__ import annotations

import time
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from compute_kernel import ewma_variance  # noqa: E402

def main() -> None:
    r = np.ascontiguousarray(np.sin(np.arange(3000) * 0.001) * 0.02)
    lam = 0.94
    t0 = time.perf_counter()
    for _ in range(200):
        ewma_variance(r, lam)
    py_s = time.perf_counter() - t0
    try:
        import arch_framework_for_volatility_models_in_quantitative_finance_rs as rs
    except ImportError:
        print("Build: maturin develop --release -m rust/py/Cargo.toml")
        print(f"Python {py_s:.3f}s")
        return
    rs_s = rs.bench_kernel_py(r, lam, 500)
    print(f"Python {py_s:.3f}s Rust {rs_s:.3f}s speedup {py_s / max(rs_s, 1e-9):.1f}x")
    np.testing.assert_allclose(
        ewma_variance(r, lam), np.asarray(rs.ewma_variance_py(r, lam)), rtol=1e-10
    )
    print("Correctness: OK")

if __name__ == "__main__":
    main()
