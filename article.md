# ARCH Framework for Volatility Models in Quantitative Finance Markets do not move with constant force. Their volatility --- the size
of price changes --- fluctuates over time. Traders see it. Charts
show...

::::### ARCH Framework for Volatility Models in Quantitative Finance 

#### Explaining volatility clustering and asymmetric shocks with ARCH-type models
Markets do not move with constant force. Their volatility --- the size
of price changes --- fluctuates over time. Traders see it. Charts show
it. Econometricians model it.

ARCH models began with a simple idea: model volatility, not just
returns. In the early 1980s, Robert Engle proposed that large shocks
tend to be followed by large shocks, even if the direction of the move
is random. This was the key to volatility clustering.

ARCH models are popular because they match real data better than
constant-variance models. They are simple to estimate and interpret.
Traders use them to improve forecasting for risk management, options
pricing, and portfolio allocation. The models also allow volatility to
respond to recent events.

ARCH models treat volatility as a dynamic process --- one that evolves,
learns, and forgets. That aligns with how markets behave.

### The Original GARCH Model
The original model is ARCH(q). It assumes today's variance depends on
past squared returns:


This captures short-term volatility persistence. But it requires a lot
of lags for long memory. Bollerslev extended it to GARCH(p, q), adding
lagged variances:


Now volatility reacts to both past shocks (ARCH) and its own past levels
(GARCH). This model became the default for financial time series.

If α1+β1\<1, volatility eventually returns to a long-run average. If the
sum is near 1, volatility persists --- a feature of many markets.

### What Makes a Model an ARCH Model?
Three elements define an ARCH-type model:

1.  [**Conditional Heteroskedasticity.** Variance is not fixed. It
    changes over time, depending on past values.]
2.  [**Dependence on Past Errors.** The model uses r\_{t-i}², the size
    of past returns, not just their sign.]
3.  [**Recursion.** The model updates volatility iteratively, with each
    new observation.]

ARCH models focus on second moments. They do not predict return
direction. They model uncertainty --- and how it moves.

### Asymmetric ARCH Models
Markets react differently to good and bad news. A sharp drop in price
increases volatility more than a similar gain. Standard GARCH cannot
handle this asymmetry.

Several extensions address the problem:

- **EGARCH (Exponential GARCH).** Models the log of variance. Allows
  negative shocks to have larger impact.


- **GJR-GARCH.** Adds a dummy for negative returns:


These models are essential for equity data, where downturns drive
volatility.

### Econometric Methods
ARCH models are estimated using Maximum Likelihood. The likelihood is
based on assuming returns are conditionally normal:


The log-likelihood for T observations is:


Optimization algorithms find the parameters that maximize L\\mathcal{L}.
You can evaluate fit using residual diagnostics, likelihood ratio tests,
and out-of-sample forecasting.

Model selection relies on AIC, BIC, and testing for remaining ARCH
effects in residuals. If squared residuals are still autocorrelated, the
model is misspecified.
::::ARCH models explain one of the most robust facts in finance: volatility
clusters. Returns are noisy, but their size is not random. GARCH models
this memory with a recursive process. Extensions like EGARCH and
GJR-GARCH capture asymmetry. Estimation uses likelihood methods and
residual tests.

ARCH models do not predict returns. They predict risk. That is often
more useful. Markets may not be predictable --- but their uncertainty
often is.
::::::::::::By [Kyle Jones](https://medium.com/@kyle-t-jones) on
[June 18, 2025](https://medium.com/p/2dba4155ee09).

[Canonical
link](https://medium.com/@kyle-t-jones/arch-framework-for-volatility-models-in-quantitative-finance-2dba4155ee09)

Exported from [Medium](https://medium.com) on November 10, 2025.
