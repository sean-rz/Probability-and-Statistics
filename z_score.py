from scipy import stats

z = 0.70  # z-score
percentile = stats.norm.cdf(z)
print(percentile)


# reverse procudre

p = 0.95 # percentile
z_sc = stats.norm.ppf(p)   # z-score
print(z_sc)