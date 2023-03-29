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
    then casts to int.
    :param range_string: string in form "year1 -- year2"
    :return: tuple (year1, year2)
    """
    i = range_string.index(" ")
    year_1 = int(range_string[:i])
    year_2 = int(range_string[i+4:])
    return [year_1, year_2]


def update_period(dataframe, periods_dict):
    for range_string in dataframe['RANGE']:
        range_tuple = range_to_tuple(range_string)
        find_me = (dataframe['RANGE'] == range_string)
        for period, ranges in periods_dict.items():
            if range_tuple in ranges:
                dataframe.loc[find_me, 'PERIOD'] = period

    return dataframe
