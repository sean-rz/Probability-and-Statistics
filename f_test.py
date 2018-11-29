from scipy import stats

alpha = 0.05
# dfn = df_groups = n_groups - 1
# dfd = df_error = (n_rows - 1) * n_groups

a = [11, 16, 9, 14, 10]   # 2% discount
b = [21, 15, 23, 10, 16]  # 1% discount
c = [14, 11, 18, 16, 21]  # no discount

f_value = stats.f_oneway(a,b,c).statistic
print(f_value)    # 2.121212121212121
f_critical = stats.f.ppf(1-alpha, dfn=2, dfd=12)
print(f_critical) # 3.8852938346523933

'''
If f_value < f_critical, we fail to reject the null hypothesis
H0: mu_A = mu_B = mu_C
or
H0: Var(A) = Var(B) = Var(C)
'''