import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

## Set seed for reproducibility
np.random.seed(101)

## Generate data
X = chi2.rvs(4, size = 50)

## hist1; default bin count (seems to be 10)
plt.figure()

plt.hist(
    X
)

plt.xlabel("X")
plt.ylabel("Count")

plt.savefig("../../fig/05_hist1.png")
plt.close()

## hist2; more bins (20)
plt.figure()

plt.hist(
    X,
    bins = 20
)

plt.xlabel("X")
plt.ylabel("Count")

plt.savefig("../../fig/05_hist2.png")
plt.close()
