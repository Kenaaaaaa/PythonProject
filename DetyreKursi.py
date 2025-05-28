import matplotlib.pyplot as plt
import numpy as np


# Përdorim të dhënat nga më sipër
h = 0.1
k = 0.01
alpha = 0.5
x = np.arange(0, 1 + h, h)
steps = int(1.0 / k)
times = [0, 0.5, 1.0]
# Funksioni për rifillim të zgjidhjes
u = np.zeros((steps + 1, len(x)))
for i, xi in enumerate(x):
   u[0, i] = 2*xi if xi <= 0.5 else 2*(1 - xi)
for n in range(steps):
   t = n * k
   u[n, 0], u[n, -1] = t, t**2
   for i in range(1, len(x)-1):
       u[n+1, i] = u[n, i] + alpha * k * (u[n, i+1] - 2*u[n, i] + u[n, i-1]) / (h**2)
   u[n+1, 0], u[n+1, -1] = t + k, (t + k)**2


# 1. Grafiku: Profil i u(x) për t=0, 0.5, 1.0
plt.figure()
for t in times:
   n_idx = int(t / k)
   plt.plot(x, u[n_idx, :], label=f"t={t}")
plt.xlabel("x")
plt.ylabel("u(x,t)")
plt.title("Profili i temperaturës u(x,t) në kohë të ndryshme")
plt.legend()
plt.show()


# 2. Grafiku: Evolucioni u(t) për x fikse
plt.figure()
time = np.arange(0, 1.0 + k, k)
for xi in [0.2, 0.5, 0.8]:
   i = int(xi / h)
   plt.plot(time, u[:, i], label=f"x={xi}")
plt.xlabel("t")
plt.ylabel("u(t) në x fikse")
plt.title("Evolucioni i temperaturës në kohë për vlera fikse të x")
plt.legend()
plt.show()

