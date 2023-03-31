from matplotlib import pyplot as plt
import seaborn as sns
import ptitprince as pt
from . import plotting_helpers as hp
from . import color as clr


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


def raincloud_plot(df, bone_type):
    # x MÜSSEN die kategorischen Daten sein
    dx = "PERIOD"
    dy = "MEASURE"

    # 'orient' horizontal (h) or vertical (v)
    ort = "h"

    # 'move' moves the datapoints below the box for better visibility
    mv = .2

    # 'palette' is the color-palette
    pal = "Set2"

    # 'sigma' adjusts the smoothing kernel used to generate the probability distribution function of the data
    sigma = .2

    g = sns.FacetGrid(df, col="MEASTYPE", col_wrap=2, sharex=False, height=6).set_axis_labels(x_var="Size in mm")
    g = g.map_dataframe(pt.RainCloud, x=dx, y=dy, data=df, palette=pal,
                        order=["Modern", "Medieval", "Roman - Saxon", "Bronze - Iron Age"],
                        orient=ort, move=mv, pointplot=True)

    g.set_titles(col_template='{col_name}-Measure', row_template='{row_name}')
    g.fig.suptitle(str(bone_type), fontsize='xx-large')
    g.fig.tight_layout()
    plt.savefig("../results/plots/rainclouds/" + bone_type + ".png")


def seaborn_vertical_barchart(data):
    plt.figure(figsize=(8, 8))

    b = sns.barplot(x='amount', y='bone_type', hue='amt_type', data=data, ci=None)
    b.set(xlabel="Menge", ylabel="Knochentyp", title="Menge an Funden und Maßen pro Knochentyp")
    plt.savefig("../results/plots/amounts_barchart.png")
