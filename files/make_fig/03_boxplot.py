import numpy as np
import matplotlib.pyplot as plt

np.random.seed(101)
X1 = np.random.random(20)
X2 = np.concatenate(
    (0.25 * np.random.random(15) + 0.25,
     [0, 0.02, 0.9, 0.95, 0.99])
)

## Single boxplot
plt.figure()
plt.boxplot(X1)

plt.xlabel("X")
plt.ylabel("Value")

plt.savefig("../../fig/05_boxplot1.png")
plt.close()

## Two boxplots
plt.figure()
plt.boxplot(
    [X1, X2]
)

plt.xlabel("X")
plt.ylabel("Value")

plt.savefig("../../fig/05_boxplot2.png")
plt.close()
