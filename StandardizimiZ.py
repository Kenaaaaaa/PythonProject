import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parametrat e shpërndarjes
mu = 100      # Mesatarja
sigma = 15    # Devijimi standard

# Vlerat për boshtin X
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# Dendësia e probabilitetit (PDF) e shpërndarjes normale
pdf = norm.pdf(x, mu, sigma)

# Grafik i shpërndarjes
plt.figure(figsize=(8,5))
plt.plot(x, pdf, label='Shpërndarja normale\nμ=100, σ=15')

# Zonat nën kurbë për a) X < 100 dhe b) X < 80
x_fill_a = np.linspace(mu - 4*sigma, 100, 1000)
plt.fill_between(x_fill_a, norm.pdf(x_fill_a, mu, sigma), alpha=0.3, label='X < 100 (50%)')

x_fill_b = np.linspace(mu - 4*sigma, 80, 1000)
plt.fill_between(x_fill_b, norm.pdf(x_fill_b, mu, sigma), alpha=0.5, label='X < 80 (~9.18%)')

# Shenjat për mesataren dhe 80
plt.axvline(mu, color='blue', linestyle='--', label='μ = 100')
plt.axvline(80, color='red', linestyle='--', label='X = 80')

plt.title('Shpërndarja normale e pikëve të testit të inteligjencës')
plt.xlabel('Pikët e testit')
plt.ylabel('Dendësia e probabilitetit')
plt.legend()
plt.grid(True)
plt.show()
