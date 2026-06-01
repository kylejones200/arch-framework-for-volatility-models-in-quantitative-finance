//! EWMA variance for volatility forecasting.

pub fn ewma_variance(returns: &[f64], lambda: f64) -> Vec<f64> {
    let n = returns.len();
    if n == 0 {
        return vec![];
    }
    let mut h = vec![0.0; n];
    h[0] = returns[0] * returns[0];
    for t in 1..n {
        h[t] = lambda * h[t - 1] + (1.0 - lambda) * returns[t - 1] * returns[t - 1];
    }
    h
}
