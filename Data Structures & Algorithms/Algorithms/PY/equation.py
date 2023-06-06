import numpy as np
import matplotlib.pyplot as plt

# input data
# x = np.array([5, 10, 100, 1000, 10000, 30000, 50000, 75000])
# y = np.array([6.81E-06, 4.00E-05, 5.23E-04, 5.06E-02, 7.443099579, 79.15471226, 260.3663071, 564.8577733])
x = np.array([10000, 30000, 50000, 75000])
y = np.array([7.443099579, 79.15471226, 260.3663071, 564.8577733])

# log transformation
X = np.log(x)
Y = np.log(y)

# linear regression
B, A = np.polyfit(X, Y, 1)
# estimated parameters
a = np.exp(A)
b = B


def f(x):
    # equation of the graph
    return a * x ** b


# plot the data and the fitted curve
plt.scatter(x, y)
plt.plot(x, f(x))
plt.xlabel('Objects')
plt.ylabel('Time (s)')
plt.show()

# print the equation
print(f'Time (s) = {a:.2e} * Objects^{b:.2f}')

"""
Sources:

https://stackoverflow.com/questions/53024952/python-get-equation-of-graph-given-coordinates
"""