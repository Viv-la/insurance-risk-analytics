from scipy import stats

def run_ttest(group_a, group_b):
    return stats.ttest_ind(group_a, group_b)

def run_anova(*groups):
    return stats.f_oneway(*groups)