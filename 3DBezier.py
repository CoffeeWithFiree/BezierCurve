import matplotlib.pyplot as plt
import numpy as np

lut = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1]
]

def Binomial(n, k):
    while n >= len(lut):
        s = len(lut)
        nextRow = [1] * (s + 1)
        for i in range(1, s):
            nextRow[i] = lut[s - 1][i - 1] + lut[s - 1][i]
        lut.append(nextRow)
    return lut[n][k]

def Bezier(n, t, w, r):
    sum_ = 0
    basis = 0
    for k in range(n):
        basis += Binomial(n - 1, k) * ((1 - t) ** (n - 1 - k)) * (t ** k) * r[k]
    for k in range(n):
        sum_ += Binomial(n - 1, k) * ((1 - t) ** (n - 1 - k)) * (t ** k) * w[k] * r[k]
    return sum_ / basis

# Weights
#weight = np.array([(110, 150, 100), (25, 190, 120), (210, 250, 160), (210, 30, 200)])  # 3D
weight = np.array([(30, 60, 100), (180, 55, 120), (30, 192, 160), (219, 223, 200)])
ratio = [0.16, 1.23, 1.39, 0.24]

# Building a Bezier curve
t_values = np.linspace(0, 1, 100)
points = np.array([Bezier(len(weight), t, weight[:, 0], ratio) for t in t_values]), \
         np.array([Bezier(len(weight), t, weight[:, 1], ratio) for t in t_values]), \
         np.array([Bezier(len(weight), t, weight[:, 2], ratio) for t in t_values])

# Plotting the Bezier curve
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(points[0], points[1], points[2], label='Bezier Curve', color='b')
ax.scatter(*weight.T, label='Control Points', color='r', marker='o')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()