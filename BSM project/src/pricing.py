import numpy as np
import scipy.stats as si

def call_price(S0, K, T, r, sigma):
    d1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T)/(sigma/np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return S0*si.norm.cdf(d1,0,1) - K*np.exp(-r*T)*si.norm.cdf(d2,0,1)
        
def put_price(S0, K, T, r, sigma):
    d1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T)/(sigma/np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return (K*np.exp(-r*T)*si.norm.cdf(-d2,0,1) - S0*si.norm.cdf(-d1,0,1))

