import matplotlib.pyplot as plt
import numpy as np


class CreditCalculator:
  
  def __init__(self, kaufPreis, nebenKosten, eigenKapital, zinsBindung, sollSinz, anfangsTilgung, sonderTilgung) -> None:
    
    self.kaufPreis = kaufPreis
    self.nebenKosten = nebenKosten
    self.eigenKapital = eigenKapital
    self.zinsBindung = zinsBindung
    self.sollZins = sollSinz
    self.anfangsTilgung = anfangsTilgung
    self.sonderTilgung = sonderTilgung
    
      
  def computeYearlyRates(self):
    
    gesamtPreis = self.kaufPreis * (1 + self.nebenKosten/100)
    gesamtSchulden = gesamtPreis - self.eigenKapital
    restSchulden = gesamtSchulden
    # compute yearly rate from the interest and debt reduction
    rate = restSchulden * ((self.sollZins + self.anfangsTilgung) / 100)
    print(r'Monthly rate is {0}'.format(rate / 12))
    rates = []

    idx = 0
    for i in range(self.zinsBindung):
      
      if restSchulden <= 0:
        break
      zinsSatz = restSchulden * (self.sollZins / 100)
      schuldSatz = rate - zinsSatz
      rTuple = (zinsSatz ,schuldSatz, restSchulden)
      rates.append(rTuple)
      restSchulden = restSchulden - schuldSatz
      # extra payment?
      restSchulden = restSchulden - self.sonderTilgung[idx]
      idx = idx + 1
      print(r'Debt after {0} year: {1}'.format(idx, restSchulden))
      
    return rates
  
  def visualizeYearlyRates(self, rates):
    
    # creating the three arrays
    zinsen = []
    schulden = []
    rest = []
    X = range(len(rates))
    for rate in rates:
      zinsen.append(rate[0])
      schulden.append(rate[1])
      rest.append(rate[2])

    plt.plot(X, zinsen)
    plt.plot(X, schulden)
    plt.plot(X, rest)
    plt.show()

    None
    

      
      
      
      
    
    
    
  