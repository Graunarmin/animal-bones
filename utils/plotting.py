from matplotlib import pyplot as plt
import plotting_helpers as hp
import color as clr


def vertical_bar_chart(x_data, y_data, title, data_label, label_rotation_threshold=10):
    """
    Creates a barchart
    :param x_data: data for the x-position of the bar
    :param y_data: data for the bar-length
    :param title: title of the plot
    :param data_label:
    :param label_rotation_threshold: if there are more values than this on x, rotate the labels
    :return:
    """
    fig, ax = plt.subplots()

    x_indexes = hp.create_indexes_from_list_values(x_data)
    bar_width = 0.25

    ax.bar(x_indexes, y_data, width=bar_width, color=clr.Color.PINK, label=data_label)

    ax.set_xticks(ticks=x_indexes, labels=x_data)

    if len(x_data) > label_rotation_threshold:
        for tick in ax.get_xticklabels():
            tick.set_rotation(45)

    __show_plot(ax, fig, title)


def horizontal_bar_chart(x_data, y_labels, title):
    """
    Creates a horizontal barchart
    :param x_data: data for the bar-length
    :param y_labels: labels on the y-axis
    :param title: title of the plot
    :return:
    """
    fig, ax = plt.subplots()
    ax.barh(x_data, y_labels)

    __show_plot(ax, fig, title)


def simple_pie_chart(slices, labels, title):
    """
    Creates a simple pie chart
    :param slices: the data that is supposed to be depicted as the slices of the pie
    :param labels: the names of the individual slices
    :param title: the title of the plot
    :return: noting
    """
    fig, ax = plt.subplots()
    ax.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'})

    __show_plot(ax, fig, title)


def __show_plot(fig, ax, title, xlabel='none', ylabel='none'):
    plt.style.use("fivethirtyeight")

    ax.set_title(title)
    if xlabel != 'none':
        ax.set_xlabel(xlabel)

    if ylabel != 'none':
        ax.set_ylabel(ylabel)

    plt.tight_layout()
    plt.show()
