# sklearn-progestimator
![Python >=3.5](https://img.shields.io/badge/Python-%3E%3D3.5-informational)
![MIT License](https://img.shields.io/badge/License-MIT-brightgreen)

A scikit-learn estimator which wraps a base estimator to provide facilities for 
time series problems where previous predictions are used as features.

---

My other goal here is to use this as a toy project for learning standard 
tools for Python development (`pytest`, `tox`, `setuptools`, `pdb`)

## Installation

TODO: Make `pip`/`conda` installable

## Usage

When calling `estimator.fit(X,y)`, `y` with time lag 1 is appended to `X`.
When calling `estimator.predict(X)`, for each sample in X, the prediction
is made using as an additional feature the previous for `y` (either true 
or predicted).

This wrapper implements the standard `estimator` API. As such, it should play well with the rest of scikit-learn.
```python
>>> from sklearn.linear_model import LinearRegression
    from progestimator.prog_regression import ProgressiveRegression
    y = np.array([[1.0], [3.0], [4.0], [7.0], [15.0], [31.0]])
    X = np.ones(([1.0], [1.0], [1.0], [1.0], [1.0], [1.0]])
    model = ProgressiveRegression(LinearRegression()) 
    model.fit(X,y)

>>> model.predict(([1.0], [1.0], [1.0], [1.0], [1.0], [1.0]]))

array([[  64.98224852],
       [ 137.08896047],
       [ 290.09172322],
       [ 614.74728963],
       [1303.63182285],
       [2765.37143003]])
```

## Development

### Environment
 
Create the development environment and activate it
```bash
conda env create -f environment.yml
conda activate progregressor-dev
```

### Tests

In `tests`
```bash
python -m pytest
```
