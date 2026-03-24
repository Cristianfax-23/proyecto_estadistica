# Tarea 4 - Distribuciones de Probabilidad
# Autor: Cristian Daniel Toro Navarro

import math
from scipy.stats import norm

print("=== 1. DISTRIBUCIÓN BINOMIAL ===")

n = 5
p = 1/6

# i) P(X = 2)
k = 2
P_X_2 = math.comb(n, k) * (p**k) * ((1-p)**(n-k))
print(f"P(X=2) = {P_X_2:.4f}")

# ii) P(X <= 1)
P_0 = (1-p)**5
P_1 = math.comb(5,1)*(p)*((1-p)**4)
P_leq_1 = P_0 + P_1
print(f"P(X<=1) = {P_leq_1:.4f}")

# iii) P(X >= 2)
P_geq_2 = 1 - P_leq_1
print(f"P(X>=2) = {P_geq_2:.4f}")


print("\n=== 2. DISTRIBUCIÓN DE POISSON ===")

lam = 1

# P(X >= 2) = 1 - P(0) - P(1)
P_0 = math.exp(-lam)
P_1 = math.exp(-lam) * lam
P_geq_2 = 1 - (P_0 + P_1)

print(f"P(X>=2) = {P_geq_2:.4f}")


print("\n=== 3. DISTRIBUCIÓN NORMAL ===")

mu = 100
sigma = 10
x = 115

# usando scipy
P_normal = norm.cdf(x, mu, sigma)
print(f"P(X<115) = {P_normal:.4f}")


print("\n=== 4. PROBABILIDAD CONJUNTA DISCRETA ===")

# Todos los pares posibles
pares = [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1),(3,0),(3,1)]

# Filtrar los que cumplen X+Y <= 2
favorables = [p for p in pares if p[0] + p[1] <= 2]

prob_discreta = len(favorables) * (1/8)

print(f"P(X+Y<=2) = {prob_discreta:.4f}")
print(f"Pares favorables: {favorables}")


print("\n=== 5. PROBABILIDAD CONJUNTA CONTINUA ===")

# Resultado analítico ya calculado:
P_continua = 0.5

print(f"P(X+Y<=1) = {P_continua:.4f}")