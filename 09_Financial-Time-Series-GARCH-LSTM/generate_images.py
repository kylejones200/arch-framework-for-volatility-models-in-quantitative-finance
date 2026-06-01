"""
Generated script to create Tufte-style visualizations
"""

import logging
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

images_dir = Path(__file__).parent / "images"
images_dir.mkdir(exist_ok=True)
original_savefig = plt.savefig


def savefig_tufte(filename, **kwargs):
    """Wrapper to save figures in images directory with Tufte style."""
    path = Path(filename)
    if not path.is_absolute() and "images" not in path.parts:
        path = images_dir / path.name
    original_savefig(path, **kwargs)
    logger.info("Saved: %s", path)


def _synthetic_returns(n: int = 500) -> np.ndarray:
    rng = np.random.default_rng(42)
    return rng.normal(0, 0.01, n)


def main() -> None:
    plt.savefig = savefig_tufte
    np.random.seed(42)
    returns = _synthetic_returns()
    try:
        from arch import arch_model

        garch_model = arch_model(returns * 100, vol="Garch", p=1, q=1)
        result = garch_model.fit(disp="off")
        cond_vol = result.conditional_volatility
    except ImportError:
        logger.warning("arch not installed; using rolling volatility proxy")
        import pandas as pd

        cond_vol = pd.Series(returns).rolling(20).std().bfill().values * 100

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(cond_vol, color="black", linewidth=0.8)
    ax.set_title("GARCH conditional volatility (or proxy)")
    ax.set_xlabel("Time")
    ax.set_ylabel("Volatility")
    plt.tight_layout()
    plt.savefig("garch_volatility.png")
    plt.close(fig)
    logger.info("All images generated successfully!")


if __name__ == "__main__":
    main()
