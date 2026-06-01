use arch_framework_for_volatility_models_in_quantitative_finance_core::ewma_variance;

fn main() {
    let r: Vec<f64> = (0..3000).map(|i| (i as f64 * 0.001).sin() * 0.02).collect();
    for _ in 0..500 {
        let _ = ewma_variance(&r, 0.94);
    }
}
