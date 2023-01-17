import json
import os

from src.CreditCalculator import CreditCalculator


currentPath = os.getcwd()
kaufKreditData = json.load(open(os.path.join(currentPath, 'data\\input.json')))

calculator = CreditCalculator(
  kaufKreditData['kaufPreis'],
  kaufKreditData['kaufNebenKostenProzent'],
  kaufKreditData['eigenKapital'],
  kaufKreditData['zinsBindung'],
  kaufKreditData['sollZinsProzent'],
  kaufKreditData['anfangsTilgungProzent'],
  kaufKreditData['sonderTilgung'])

rates = calculator.computeYearlyRates()

print('Rates')
for rate in rates:
  print(r'{0}; {1}; {2}'.format(rate[0], rate[1], rate[2]))
  
calculator.visualizeYearlyRates(rates)