from scipy import stats

alpha = 0.05
# dfn = df_groups = n_groups - 1
# dfd = df_error = (n_rows - 1) * n_groups

f_critical = stats.f.ppf(1-alpha, dfn=2, dfd=27)

'''
If f_value < f_critical, we fail to reject the null hypothesis
H0: mu_A = mu_B = mu_C
or
H0: Var(A) = Var(B) = Var(C)
'''