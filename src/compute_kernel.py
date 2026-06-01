"""EWMA variance for volatility forecasting."""

from __future__ import annotations

import numpy as np


def ewma_variance(returns: np.ndarray, lam: float) -> np.ndarray:
    r = np.asarray(returns, dtype=float)
    n = len(r)
    if n == 0:
        return np.empty(0, dtype=float)
    h = np.zeros_like(r)
    h[0] = r[0] ** 2
    for t in range(1, n):
        h[t] = lam * h[t - 1] + (1.0 - lam) * r[t - 1] ** 2
    return h
