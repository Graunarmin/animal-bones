from scipy import stats
import statistics
import math
from . import load_write as lw


def compute_t_test(x1, x2):
    """
    Calculate the T-test for the means of two independent samples of scores.
    This is a two-sided test for the null hypothesis that 2 independent samples
    have identical average (expected) values.
    (Assume different variances)
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html
    :param x1:
    :param x2:
    :return:
    """
    return stats.ttest_ind(x1, x2, equal_var=False)


def ttest(df, bone_type):
    meas_grp = df.groupby('MEASTYPE')
    alpha = 0.1
    p_values = {}

    for meastype in meas_grp.groups.keys():
        period_grp = meas_grp.get_group(meastype).groupby('PERIOD')
        valid_periods = []
        p_values[meastype] = {}

        for period in period_grp.groups.keys():
            period_data = period_grp.get_group(period)
            if len(period_data['MEASURE']) > 3:
                shapiro = stats.shapiro(period_data['MEASURE'])
                #if shapiro.pvalue < alpha:
                #    print(meastype, "in", period, ": Daten nicht normalverteilt")
                #else:
                valid_periods.append(period)

        if len(valid_periods) > 2:
            for i in range(len(valid_periods) - 1):
                per_1 = valid_periods[i]
                p_values[meastype][per_1] = {}
                for j in range(i + 1, len(valid_periods)):
                    per_2 = valid_periods[j]
                    data_1 = period_grp.get_group(per_1)['MEASURE']
                    data_2 = period_grp.get_group(per_2)['MEASURE']
                    p_value = compute_t_test(data_1, data_2)[1]
                    p_values[meastype][per_1][per_2] = [p_value,
                                                        "signifikant" if p_value < alpha else "nicht signifikant"]

    lw.save_json(p_values, "../results/statistics/" + bone_type + "_statistics.json")
