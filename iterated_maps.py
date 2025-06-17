import matplotlib.pyplot as plt

# Logistic map: x_{n+1} = r * x_n * (1 - x_n)
def logistic_map(r, x0, n):
    xs = [x0]
    for i in range(n - 1):
        x_next = r * xs[-1] * (1 - xs[-1])
        xs.append(x_next)
    return xs

# Parameters
r = 3.9           # Control parameter (try values between 2.5 and 4.0)
x0 = 0.1          # Initial condition (between 0 and 1)
n = 100           # Number of iterations

# Compute iterates
x_vals = logistic_map(r, x0, n)

# Plot
plt.figure(figsize=(10, 4))
plt.plot(range(n), x_vals, marker='o', markersize=3, linestyle='-', color='royalblue')
plt.title(f'Logistic Map: r = {r}, x₀ = {x0}')
plt.xlabel('Iteration (n)')
plt.ylabel('xₙ')
plt.grid(True)
plt.tight_layout()
plt.show()


