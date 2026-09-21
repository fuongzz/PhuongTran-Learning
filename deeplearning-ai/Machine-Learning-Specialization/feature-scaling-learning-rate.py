import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=2)

X_train = np.array([
    [952,  2, 1, 65], [1244, 3, 1, 64], [1947, 3, 2, 17],
    [1725, 3, 2, 42], [1959, 3, 2, 15], [1314, 2, 1, 14],
    [864,  2, 1, 66], [1836, 3, 1, 17], [1026, 3, 1, 43],
    [3194, 4, 2, 87], [1300, 3, 1, 15], [1200, 3, 1, 53],
])

print(X_train.shape)

print(X_train.shape[0])

print(X_train.shape[1])

y_train = np.array([271.5, 300, 509.8, 394, 540, 415, 230, 560, 294, 718.2, 391.4, 350])
X_features = ['size(sqft)', 'bedroom', 'floors', 'age']

def compute_cost(X, y, w, b):
    m = X.shape[0]
    err = X @ w + b - y
    return (err ** 2).sum() / (2 * m)

def compute_gradient(X, y, w, b):
    m = X.shape[0]
    err = X @ w + b - y
    dj_dw = X.T @ err / m
    dj_db = err.sum() / m
    return dj_dw, dj_db

def gradient_descent(X, y, w, b, alpha, num_iters):
    J_hist = []
    for i in range(num_iters):
        dj_dw, dj_db = compute_gradient(X, y, w, b)
        w = w - alpha * dj_dw
        b = b - alpha * dj_db
        J_hist.append(compute_cost(X, y, w, b))
        if i % (num_iters // 10) == 0:
            print(f"Iter {i:5d}: cost {J_hist[-1]:.2e}, w {w}, b {b:.2f}")

    return w, b, J_hist

w0, b0 = np.zeros(4), 0.0

w, b, J = gradient_descent(X_train, y_train, w0, b0, alpha = 9.9e-7, num_iters=10)