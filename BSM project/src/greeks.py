import numpy as np
import scipy.stats as si

def param(S0, K, T, r, sigma):
    d1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T)/(sigma/np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    delta_call = si.norm.cdf(d1,0,1)
    delta_put = si.norm.cdf(d1,0,1) - 1

    gamma = si.norm.pdf(d1,0,1)/(S0*sigma*np.sqrt(T))
    vega = S0*si.norm.pdf(d1,0,1)*np.sqrt(T)

    return delta_call, delta_put, gamma, vega

   


S0 = 100     # prix spot de l'actif
K = 105      # prix d'exercice (strike)
T = 1        # maturité en années
r = 0.05     # taux sans risque (5%)
sigma = 0.2  # volatilité (20%)
delta_call, delta_put, gamma, vega = param(S0, K, T, r, sigma)
print ("delta_call: ", delta_call) 
print ("delta_put: ", delta_put)
print ("gamma: ", gamma)
print ("vega: ", vega)