from scipy.stats import ttest_ind

a = [1136, 1178, 1212, 1193, 1226, 1154, 1230, 1222, 1161, 1148]
b = [1184, 1203, 1219, 1238, 1243, 1204, 1269, 1256, 1156, 1248]

t_value = ttest_ind(a,b).statistic  # t-score for two-tailed
p_value_one_tailed = ttest_ind(a,b).pvalue/2  # p/2 < alpha

print(p_value_one_tailed)  # 0.0175