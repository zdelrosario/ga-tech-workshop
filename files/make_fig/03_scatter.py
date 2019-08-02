import numpy as np
import matplotlib.pyplot as plt

n_samp = 200

## Set seed for reproducibility
np.random.seed(101)

## Generate data
sigma = np.array([2, 1]) # Standard deviations
Rho1  = np.array([
    [  1, 0.5],
    [0.5,   1]
])
Rho2  = np.array([
    [  1, 0.9],
    [0.9,   1]
])

X1 = np.random.multivariate_normal(
    mean = np.zeros(2),
    cov  = np.dot(np.diag(sigma), np.dot(Rho1, np.diag(sigma))),
    size = n_samp
)

X2 = np.random.multivariate_normal(
    mean = np.zeros(2),
    cov  = np.dot(np.diag(sigma), np.dot(Rho2, np.diag(sigma))),
    size = n_samp
)

X3 = np.zeros((n_samp, 2))
X3[:, 0] = 2 * np.random.random(size = n_samp) - 1
X3[:, 1] = 1.5 * np.power(X3[:, 0], 2) - 0.5 + np.random.normal(size = n_samp) * 0.1

X4 = np.random.multivariate_normal(
    mean = np.zeros(3),
    cov  = np.array([
        [  1, 0.7, 0.7],
        [0.7,   1, 0.7],
        [0.7, 0.7,   1]
    ]),
    size = n_samp
)

# Check correlation in X3 data
print(np.corrcoef(X3.T))

## Plot data
# Moderately-correlated data
plt.figure()

plt.scatter(X1[:, 0], X1[:, 1])

plt.xlabel("X")
plt.ylabel("Y")

plt.savefig("../../fig/05_scatter1.png")
plt.close()

# Strongly-correlated data
plt.figure()

plt.scatter(X2[:, 0], X2[:, 1])

plt.xlabel("X")
plt.ylabel("Y")

plt.savefig("../../fig/05_scatter2.png")
plt.close()

# Nonlinear-related data
plt.figure()

plt.scatter(X3[:, 0], X3[:, 1])

plt.xlabel("X")
plt.ylabel("Y")

plt.savefig("../../fig/05_scatter3.png")
plt.close()

# 3-dimensional data
plt.figure()

plt.scatter(
    X4[:, 0],
    X4[:, 1],
    c = X4[:, 2],
    cmap = plt.cm.get_cmap('viridis')
)

plt.xlabel("X")
plt.ylabel("Y")
cbar = plt.colorbar()
cbar.set_label("Z")

plt.savefig("../../fig/05_scatter4.png")
plt.close()
