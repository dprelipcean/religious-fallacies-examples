import matplotlib.pyplot as plt
import numpy as np

from scripts.congregate_data import extract_data
from scripts.regression import regression_points
from scripts.plotting_scripts import default_plot_function

colors = {'blue': '#2300A8', 'yellow': '#FFFF00', 'green': '#00A658', 'red': '#FF0000'}


def default_plot(master_data, index=None, plot_function=default_plot_function, ylabel_unit='', log=False,
                 save_file=True, horizontal_ticks=None):
    """Plot the data sets with some default parameters."""
    print(f'Plotting index: {index}.')
    ylabel = f'{index} {ylabel_unit}'
    file_name = f'../figures/{index}.png'

    data_index, data_religion_level, txt = extract_data(master_data, index, 'Religion is important')

    regression_x, regression_y = regression_points(data_religion_level, data_index)

    zoom_factor = 2

    w = 7.195 * zoom_factor
    h = 3.841 * zoom_factor

    fig, ax = plt.subplots()
    fig.set_size_inches(w, h)

    plot_function(ax, data_religion_level, data_index)

    plt.xlabel("Country religiosity levels (%)")
    plt.ylabel(f"{ylabel} ")

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
    plt.plot(regression_x, regression_y, '-r', color=colors['green'])
    # ax.legend(['Data Points', 'Regression Line'])

    ax.set_xlim([0, 100])
    # ax.set_ylim([0, 100])

    # Provide tick lines across the plot to help your viewers trace along
    # the axis ticks. Make sure that the lines are light and small so they
    # don't obscure the primary data lines.
    if isinstance(horizontal_ticks, tuple):
        for data_index_value in np.linspace(*horizontal_ticks):
            plt.plot(range(0, 100), [data_index_value] * len(range(0, 100)), "--", lw=0.5, color="black", alpha=0.3)

    # Plot vertical lines for religiosity levels

    y_min = horizontal_ticks[0]
    y_max = horizontal_ticks[1]
    x_ticks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for data_religion_level in x_ticks:
        plt.plot([data_religion_level] * len(range(0, 100)), np.linspace(y_min, y_max, 100), "--", lw=0.5, color="black", alpha=0.3)


    # Remove default boxing
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    if save_file:
        fig.savefig(file_name)
    else:
        plt.show()
