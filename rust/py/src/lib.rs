use arch_framework_for_volatility_models_in_quantitative_finance_core::ewma_variance;
use numpy::{PyArray1, PyReadonlyArray1, IntoPyArray};
use pyo3::prelude::*;

#[pyfunction]
fn ewma_variance_py<'py>(py: Python<'py>, returns: PyReadonlyArray1<f64>, lam: f64) -> PyResult<Bound<'py, PyArray1<f64>>> {
    Ok(ewma_variance(returns.as_slice()?, lam).into_pyarray(py))
}

#[pyfunction]
#[pyo3(signature = (returns, lam, iterations=500))]
fn bench_kernel_py(returns: PyReadonlyArray1<f64>, lam: f64, iterations: usize) -> PyResult<f64> {
    let returns_buf = returns.as_slice()?.to_vec();
    let start = std::time::Instant::now();
    for _ in 0..iterations {
        let _ = ewma_variance(&returns_buf, lam);
    }
    Ok(start.elapsed().as_secs_f64())
}

#[pymodule]
fn arch_framework_for_volatility_models_in_quantitative_finance_rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(ewma_variance_py, m)?)?;
    m.add_function(wrap_pyfunction!(bench_kernel_py, m)?)?;
    Ok(())
}
