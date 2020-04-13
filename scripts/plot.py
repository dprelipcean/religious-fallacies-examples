import csv

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

from scripts.congregate_data import extract_data
from scripts.utils import compare_names, convert_to_number, extract_name_from_file
from scripts.regression import regression_points

colors = {'blue': '#2300A8', 'yellow': '#FFFF00', 'green': '#00A658', 'red': '#FF0000'}


def plot_education_index(master_data):
    """Plot the data sets with some default parameters."""
    index = 'EducationIndex'

    ylabel = index
    file_name = f'../figures/{index}.png'

    data_index, data_religion_level, txt = extract_data(master_data, index, 'Religion is important')

    regression_x, regression_y = regression_points(data_religion_level, data_index)

    fig, ax = plt.subplots()
    colors = {'blue': '#2300A8', 'yellow': '#FFFF00', 'green': '#00A658', 'red': '#FF0000'}

    for i in range(len(data_religion_level)):
        point_x = data_religion_level[i]
        point_y = data_index[i]

        if point_x < 60 and point_y > 0.7:
            color = colors['blue']
        elif 60 < point_x:
            color = colors['yellow']
            if point_y < 0.55:
                color = colors['red']

        else:
            color = colors['red']

        ax.plot(point_x, point_y, 'o', color=color)

    plt.xlabel("Country religiosity levels (%)")
    plt.ylabel(f"{ylabel} (a.u.)")
    # ax.set_yscale('log')

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
    # y_min = int(min(data_index) * 10)/10
    # y_max = int(max(data_index) * 10)/10 + 0.1
    y_min = 0
    y_max = 1
    n_points = int((y_max - y_min) * 10) + 1

    for data_index in np.linspace(y_min, y_max, n_points):
        plt.plot(range(0, 100), [data_index] * len(range(0, 100)), "--", lw=0.5, color="black", alpha=0.3)

    x_ticks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for data_religion_level in x_ticks:
        plt.plot([data_religion_level] * len(range(0, 100)), np.linspace(y_min, y_max, 100), "--", lw=0.5, color="black", alpha=0.3)

    # Remove default boxing
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    fig.savefig(file_name)
    plt.show()


def default_plot(master_data, index=None, ylabel_unit='', save_file=False):
    """Plot the data sets with some default parameters."""

    ylabel = f'{index} {ylabel_unit}'
    file_name = f'../figures/{index}.png'

    data_index, data_religion_level, txt = extract_data(master_data, index, 'Religion is important')

    regression_x, regression_y = regression_points(data_religion_level, data_index)

    fig, ax = plt.subplots()

    ax.plot(data_religion_level, data_index, 'o', color=colors['blue'])

    plt.xlabel("Country religiosity levels (%)")
    plt.ylabel(f"{ylabel} ")
    # ax.set_yscale('log')

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
    y_min = min(data_index)
    y_max = max(data_index)
    n_points = int((y_max - y_min) * 10) + 1

    for data_index in np.linspace(y_min, y_max, n_points):
        plt.plot(range(0, 100), [data_index] * len(range(0, 100)), "--", lw=0.5, color="black", alpha=0.3)

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


def plot_research_expenditure_absolute(master_data):
    """Plot the data sets with some default parameters."""

    index = 'Expenditures on R&D (billions of USD)'
    ylabel = f'{index}'
    file_name = f'../figures/{index}.png'

    data_index, data_religion_level, txt = extract_data(master_data, index, 'Religion is important')

    regression_x, regression_y = regression_points(data_religion_level, data_index)

    fig, ax = plt.subplots()

    ax.plot(data_religion_level, data_index, 'o', color=colors['blue'])

    plt.xlabel("Country religiosity levels (%)")
    plt.ylabel(f"{ylabel} ")
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
    y_min = min(data_index)
    y_max = max(data_index)
    n_points = int((y_max - y_min)) + 1

    y_ticks = [0.1, 1, 10, 100, 1000]
    for data_index in y_ticks:
        plt.plot(range(0, 100), [data_index] * len(range(0, 100)), "--", lw=0.5, color="black", alpha=0.3)

    x_ticks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for data_religion_level in x_ticks:
        plt.plot([data_religion_level] * len(range(0, 100)), np.linspace(y_min, y_max, 100), "--", lw=0.5, color="black", alpha=0.3)

    # Remove default boxing
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    plt.show()


def plot_research_expenditure_relative(master_data):
    """Plot the data sets with some default parameters."""
    index = '% of GDP'
    ylabel = f'{index} invested in Research and Development'
    file_name = f'../figures/{index}.png'

    data_index, data_religion_level, txt = extract_data(master_data, index, 'Religion is important')

    regression_x, regression_y = regression_points(data_religion_level, data_index)

    fig, ax = plt.subplots()

    ax.plot(data_religion_level, data_index, 'o', color=colors['blue'])

    plt.xlabel("Country religiosity levels (%)")
    plt.ylabel(f"{ylabel} ")
    # ax.set_yscale('log')

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
    y_min = 0
    y_max = 5
    y_ticks = [1, 2, 3, 4, 5]
    for data_index in y_ticks:
        plt.plot(range(0, 100), [data_index] * len(range(0, 100)), "--", lw=0.5, color="black", alpha=0.3)

    x_ticks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for data_religion_level in x_ticks:
        plt.plot([data_religion_level] * len(range(0, 100)), np.linspace(y_min, y_max, 100), "--", lw=0.5, color="black", alpha=0.3)

    # Remove default boxing
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    plt.show()
