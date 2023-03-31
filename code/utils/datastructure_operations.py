from collections import Counter
import pprint


pp = pprint.PrettyPrinter(indent=2, compact=True)


def count_amounts_in_column(dataframe, column):
    """
    Counts how often each attribute occurs in the specified column of a dataframe
    :param dataframe: the dataframe we want to look at
    :param column: the label of the column (string, all CAPS)
    :return: a dictionary with the amounts for each attribute of the column
    """
    attribute_counter = Counter()
    attribute_counter.update(dataframe.loc[:, column])
    return dict(attribute_counter)


def split_dictionary(dictionary):
    """
    Splits a dictionary into two separate lists,
    the first of which contains the keys, the second the respective values.
    :param dictionary: the dictionary to be split up
    :return: two lists, the first contains all keys, the second all values
    """
    return list(dictionary.keys()), list(dictionary.values())


def pretty_print(text):
    pp.pprint(text)


def range_to_tuple(range_string):
    """
    Slices a string of two integer years into a tuple.
    First slices the string so only the number values and their algebraic sign remain,
    then casts to int
    :param range_string: string in form "year1 -- year2"
    :return: list [year1, year2]
    """
    i = range_string.index(" ")
    year_1 = int(range_string[:i])
    year_2 = int(range_string[i+4:])
    return [year_1, year_2]


def update_period(dataframe, periods_dict):
    """
    Updates the values in the 'PERIOD' column to be
    one of the four periods we summarized.
    Also deletes all columns we no longer need.
    :param dataframe:
    :param periods_dict:
    :return:
    """
    for range_string in dataframe['RANGE']:
        range_tuple = range_to_tuple(range_string)
        find_me = (dataframe['RANGE'] == range_string)
        for period, ranges in periods_dict.items():
            if range_tuple in ranges:
                dataframe.loc[find_me, 'PERIOD'] = period

    df = dataframe[['BONEID', 'ELEMENT', 'MEASURE', 'MEASTYPE', 'PERIOD', 'RANGE']].copy()
    return df


def dimensions_dict(grouped_dataframe):
    """
    Creates a dictionary of separate dataframes from a grouped dataframe
    The key is the name of the group, the value another dictionary
    with "df" as key for the dataframe and "size" as key for the size
    :param grouped_dataframe:
    :param keys:
    :return:
    """
    group_names = list(grouped_dataframe.groups.keys())
    frames_dict = dict()

    for name in group_names:
        df_group = grouped_dataframe.get_group(name)
        frames_dict[name] = {
            "df": df_group,
            "size": len(df_group)
        }

    return frames_dict


def bone_type_dict(bone_type, df, bone_amt, per_amt):
    return {
        bone_type: {
            "df": df,
            "bone_amt": bone_amt,
            "meas_amt": len(df),
            "periods_amt": per_amt
        }
    }


def trim_dictionary(dictionary, trim_to):
    """
    trims the dictionary to the size of trim_to according to
    the "size"-key
    Not very elegant, I hate this. Rewrite!
    :param dictionary:
    :param trim_to:
    :return:
    """
    if len(dictionary) > trim_to:
        sizes = []
        for entry in dictionary:
            sizes.append({"name": entry, "size": dictionary[entry]["size"]})

        sizes.sort(key=lambda x: x["size"], reverse=True)
        keep = sizes[:trim_to]
        codes = []

        for entry in keep:
            codes.append(entry['name'])

        for entry in list(dictionary.keys()):
            if entry not in codes:
                del dictionary[entry]

    return dictionary


