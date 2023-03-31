import pandas as pd


def bone_type_dict(bone_type, df, bone_amt, per_amt):
    """

    :param bone_type:
    :param df:
    :param bone_amt:
    :param per_amt:
    :return:
    """
    return {
        bone_type: {
            "df": df,
            "bone_amt": bone_amt,
            "meas_amt": len(df),
            "periods_amt": per_amt
        }
    }


def create_dataframe_for_barchart(bone_types_dict):
    """
    Returns a dataframe that can be fed into a seaborn barplot
    :param bone_types_dict:
    :return:
    """
    all_amounts = []
    amt_types = []
    bone_types = []
    bone_types_long = []
    periods = []
    finding_amounts = []

    for bone_type in list(bone_types_dict.keys()):
        bones_amt = bone_types_dict[bone_type]["bone_amt"]
        meas_amt = bone_types_dict[bone_type]["meas_amt"]
        periods_amt = bone_types_dict[bone_type]["periods_amt"]

        if bones_amt < 10 or (bone_types_dict[bone_type]["periods_amt"]) <= 2:
            print(bone_type, "has not enough data.")

        else:
            print(bone_type, ":",
                  bones_amt, "Fund(e) und",
                  meas_amt, "Messungen. Datierungen für",
                  periods_amt, "Perioden.")
            all_amounts.append(bones_amt)
            amt_types.append("find")
            all_amounts.append(meas_amt)
            amt_types.append("meas")
            bone_types.append(bone_type)
            bone_types_long.append(bone_type)
            bone_types_long.append(bone_type)

            finding_amounts.append(bones_amt)
            periods.append(periods_amt)

    df_barplot_findings_and_measures = pd.DataFrame(
        {
            'amount': all_amounts,
            'amt_type': amt_types,
            'bone_type': bone_types_long
        }
    )

    df_barplot_findings_period = pd.DataFrame(
        {
            'amount': finding_amounts,
            'period': periods,
            'bone_type': bone_types
        }
    )
    return df_barplot_findings_and_measures, df_barplot_findings_period


def archaeological_periods_dict():
    return {'Late Bronze Age - Early Iron Age': [],
            'Early Iron Age': [],
            'Early - Middle Iron Age': [],
            'Middle Iron Age': [],
            'Iron Age': [],
            'Mid - Late Iron Age': [],
            'Late Iron Age': [],
            'Late Iron Age - Early Roman': [],
            'Early Roman': [],
            'Mid Roman': [],
            'Roman': [],
            'Late Roman': [],
            'Early Saxon': [],
            'Saxon': [],
            'Late Saxon': [],
            'Roman - Early Medieval': [],
            'Early Medieval': [],
            'Medieval': [],
            'Medieval - Post Medieval': [],
            'Post Medieval': [],
            'Modern': [],
            }
