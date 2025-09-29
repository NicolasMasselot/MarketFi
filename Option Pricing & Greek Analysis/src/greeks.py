import numpy as np
import scipy.stats as si

def param(S0, K, T, r, sigma):
    d1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    delta_call = si.norm.cdf(d1,0,1)
    delta_put = si.norm.cdf(d1,0,1) - 1

    gamma = si.norm.pdf(d1,0,1)/(S0*sigma*np.sqrt(T))
    vega = S0*si.norm.pdf(d1,0,1)*np.sqrt(T)

    return delta_call, delta_put, gamma, vega

#When a function returns multiple values, they are returned as a tuple. The values can be accessed using their index.
#[0] : delta_call, etc..
