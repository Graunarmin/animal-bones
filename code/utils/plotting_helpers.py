import numpy as np


def create_indexes_from_list_values(data_list):
    """
    Creates and returns a numpy array, basically a numbered version
    of the values in the data_list, so we can shift the location of
    the values on the axis (in case we want several bars from different
    datasets next to each other)
    :param data_list: the list of data to create the indexes for
    (e.g. the x-values on a vertical bar chart)
    :return: the numpy array
    """
    return np.arange(len(data_list))
