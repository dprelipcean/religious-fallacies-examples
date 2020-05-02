import matplotlib.pyplot as plt
import numpy as np

from scripts.congregate_data import extract_data
from scripts.regression import regression_points

colors = {'blue': '#2300A8', 'yellow': '#FFFF00', 'green': '#00A658', 'red': '#FF0000'}


def default_plot(master_data, index=None, index2='Religion is important', xlabel=None, ylabel=None, log=False, vertical_ticks=None,
                 save_file=True, horizontal_ticks=None, plot_regression=True, zoom_factor=2, name=None):
    """Plot the data sets with some default parameters."""
    print(f'Plotting index: {index}.')
    if not ylabel:
        ylabel = f'{index}'
    if not xlabel:
        xlabel = "Country religiosity levels (%)"

    if name:
        file_sufix = name
    else:
        file_sufix = index
    file_name = f'../figures/{file_sufix}.png'

    data_index, data_religion_level, txt = extract_data(master_data, index, index2)

    if plot_regression:
        regression_x, regression_y = regression_points(data_religion_level, data_index)
        plt.plot(regression_x, regression_y, '-r', color=colors['green'])

    w = 7.195 * zoom_factor
    h = 3.841 * zoom_factor

    fig, ax = plt.subplots()
    fig.set_size_inches(w, h)

    ax.plot(data_religion_level, data_index, 'o', color=colors['blue'])

    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

    if index2 == 'Religion is important':
        ax.set_xlim([0, 100])
        vertical_ticks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # ax.set_ylim([0, 100])

    if log:
        ax.set_yscale('log')

    # Annotate points with country text
    plt.rcParams.update({'font.size': 11})
    if txt:
        for i in range(len(txt)):
            ax.annotate(txt[i], (data_religion_level[i], data_index[i]),
                        textcoords="offset points",  # how to position the text
                        xytext=(-15, -15),  # distance from text to points (data_religion_level,data_index)
                        ha='center',  # horizontal alignment can be left, right or center
                        )
    # ax.legend(['Data Points', 'Regression Line'])


    # Provide tick lines across the plot to help your viewers trace along
    # the axis ticks. Make sure that the lines are light and small so they
    # don't obscure the primary data lines.
    if isinstance(vertical_ticks, tuple):
        x_min = horizontal_ticks[0]
        x_max = horizontal_ticks[1]
        for data_index_value in np.linspace(*vertical_ticks):
            plt.plot(np.linspace(x_min, x_max, 100), [data_index_value] * 100, "--", lw=0.5, color="black", alpha=0.3)

    # Plot vertical lines for religiosity levels
    if isinstance(horizontal_ticks, tuple):
        try:
            y_min = vertical_ticks[0]
            y_max = vertical_ticks[1]
        except TypeError:
            y_min = min(data_index)
            y_max = max(data_index)
        for data_religion_level in np.linspace(*horizontal_ticks):
            plt.plot([data_religion_level] * 100, np.linspace(y_min, y_max, 100), "--", lw=0.5, color="black", alpha=0.3)


    # Remove default boxing
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    if save_file:
        fig.savefig(file_name)
    else:
        plt.show()
