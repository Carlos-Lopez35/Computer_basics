P= 250000
annual_rate=0.05
years=30
r= annual_rate /12
n = years *12
M = P*(r*(1+r)**n) / ((1+r)**n - 1)
print ("The monthly payment for a loan of 250.000€, with an annual interest rate of 5% and a term of 30 years, is", (M),"euros")