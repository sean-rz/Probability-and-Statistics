"""
The chi-square statistical test is used to determine whether there’s a significant difference 
between an expected distribution and an actual distribution. It’s typically used with categorical 
data such as colors, or gender.
"""
from scipy.stats import chi2

alpha = 0.05   # 0.95 confidence level
df = 5         # degree of freedom = # of possible outcomes - 1 

chi2_critical = chi2.isf(alpha, df)
print(chi2_critical)

'''
If chi2 > chi2_critical, we reject the null hypothesis
H0: Observed results (frequency of events) match expectations
'''