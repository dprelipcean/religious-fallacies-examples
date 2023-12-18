import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt, cos, sin, deg2rad, isnan

from matplotlib.ticker import (MultipleLocator, AutoMinorLocator, LogLocator)

from seaborn import color_palette

from core.congregate_data import extract_data, extract_data_dataframe
from core.regression import regression_points


colors = {'blue': '#2300A8', 'yellow': '#FFFF00', 'green': '#00A658', 'red': '#FF0000'}
colors_seaborn = color_palette("Set2")


def default_all(master_data, index=None, index2='Religion is important', xlabel=None, ylabel=None, log=False, vertical_ticks=None,
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

    # data_index, data_religion_level, txt = extract_data(master_data, index, index2)
    data_index, data_religion_level, txt, continents, data_population \
        = extract_data_dataframe(master_data, index, index2)

    if False:
        w = 7.195 * zoom_factor
        h = 3.841 * zoom_factor
        fig.set_size_inches(w, h)

    fig, ax = plt.subplots(figsize=(7, 7))

    if plot_regression:
        regression_x, regression_y = regression_points(data_religion_level, data_index)
        plt.plot(regression_x, regression_y, '-r', color=colors['green'])

    if True:
        # print(master_data)
        different_continents = ["Europe"]
        # different_continents = ["Europe", "Africa", "North America", "South America", "Asia"]
        for index_continent, continent in enumerate(different_continents):
            master_data_continent = master_data.loc[master_data["Continent"] == continent]
            #print(master_data_continent)
            data_index_continent, data_religion_level_continent, txt_continent, continents, data_population\
                = extract_data_dataframe(master_data_continent, index, index2)
            # print(data_index_continent)
            # print(data_religion_level_continent)

            markersize_max_val = sqrt(max(data_population))
            markersize_min = 50
            markersize_max = 100
            markersizes = [(markersize_max - markersize_min) * sqrt(val)/markersize_max_val + markersize_min
                           for val in data_population]

            ax.scatter(data_religion_level_continent, data_index_continent,
                       marker='o',
                       #s=markersizes,
                       color=colors_seaborn[index_continent])
    else:
        ax.scatter(data_religion_level, data_index,
                   marker='o', color=colors['blue'],
                   )

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

    if False:
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

    axis_tick_length = 5
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which='major', length=2*axis_tick_length)
    ax.tick_params(which='minor', length=axis_tick_length)

    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which='major', length=2*axis_tick_length)
    ax.tick_params(which='minor', length=axis_tick_length)

    # Remove default boxing
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    if save_file:
        fig.savefig(file_name)
    else:
        plt.show()


def plot_per_continent(master_data, index=None, index2='Religion is important', xlabel=None, ylabel=None, log=False, vertical_ticks=None,
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

    # data_index, data_religion_level, txt = extract_data(master_data, index, index2)
    data_index, data_religion_level, txt, continents, data_population \
        = extract_data_dataframe(master_data, index, index2)


    # print(master_data)
    different_continents = ["Europe"]
    # different_continents = ["Europe", "Africa", "North America", "South America", "Asia"]
    for index_continent, continent in enumerate(different_continents):

        file_name = f'../figures/{continent}/{file_sufix}.png'

        fig, ax = plt.subplots(figsize=(7, 7))

        master_data_continent = master_data.loc[master_data["Continent"] == continent]
        #print(master_data_continent)
        data_index_continent, data_religion_level_continent, txt_continent, continents, data_population\
            = extract_data_dataframe(master_data_continent, index, index2)
        # print(data_index_continent)
        # print(data_religion_level_continent)

        markersize_max_val = sqrt(max(data_population))
        markersize_min = 50
        markersize_max = 100
        markersizes = [(markersize_max - markersize_min) * sqrt(val)/markersize_max_val + markersize_min
                       for val in data_population]

        ax.scatter(data_religion_level_continent, data_index_continent,
                   marker='o',
                   #s=markersizes,
                   color=colors_seaborn[index_continent])

        if plot_regression:
            regression_x, regression_y = regression_points(data_religion_level_continent, data_index_continent)
            plt.plot(regression_x, regression_y, '-r', color=colors['green'])


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
            for index_country, country_name in enumerate(txt_continent):
                ax.annotate(country_name,
                            (data_religion_level_continent[index_country], data_index_continent[index_country]),
                            textcoords="offset points",  # how to position the text
                            xytext=(-15, -15),  # distance from text to points (data_religion_level,data_index)
                            ha='left',  # horizontal alignment can be left, right or center
                            )
        # ax.legend(['Data Points', 'Regression Line'])

        axis_tick_length = 5
        ax.xaxis.set_minor_locator(AutoMinorLocator())
        ax.tick_params(which='major', length=2*axis_tick_length)
        ax.tick_params(which='minor', length=axis_tick_length)

        ax.yaxis.set_minor_locator(AutoMinorLocator())
        ax.tick_params(which='major', length=2*axis_tick_length)
        ax.tick_params(which='minor', length=axis_tick_length)

        # Remove default boxing
        for spine in plt.gca().spines.values():
            spine.set_visible(False)

        if save_file:
            fig.savefig(file_name)
        else:
            plt.show()


def plot_color_scheme(master_data):

    # print(master_data.columns)
    countries = list()
    colors = list()

    for country in master_data.index:
        if type(country) != str:
            continue
        if country == " All Countries":
            continue

        # print(country, master_data["Christians"])

        color_1_scale = master_data.at[country, "Christians"]
        color_2_scale = master_data.at[country, "Muslims"]
        color_3_scale = master_data.at[country, "Jews"]

        # print(country, color_1_scale)

        if color_1_scale == "< 1.0":
            color_1_scale = 0.01
        if color_2_scale == "< 1.0":
            color_2_scale = 0.01
        if color_3_scale == "< 1.0":
            color_3_scale = 0.01

        if color_1_scale == ">99.0":
            color_1_scale = 0.99
        if color_2_scale == ">99.0":
            color_2_scale = 0.99
        if color_3_scale == ">99.0":
            color_3_scale = 0.99

        if type(color_1_scale) == str or type(color_2_scale) == str or type(color_3_scale) == str:
            color_1_scale = float(color_1_scale)
            color_2_scale = float(color_2_scale)
            color_3_scale = float(color_3_scale)

            color_1_scale /= 100
            color_2_scale /= 100
            color_3_scale /= 100

        elif isnan(color_1_scale):
            continue

        # print(country, color_1_scale)
        countries.append(country)
        colors.append([color_1_scale, color_2_scale, color_3_scale])

    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib import cm
    import matplotlib as mpl

    fig, ax = plt.subplots(figsize=(7, 7))

    for index_country, country_name in enumerate(countries):
        a, b, c = colors[index_country]
        print(a, b, c)
        a = 2 * a - 1
        b = 2 * b - 1
        c = 2 * c - 1
        # print(type(a), type(b), type(c))
        x = a - (b + c) * cos(deg2rad(60))
        y = (b - c) * sin(deg2rad(60))
        print(x, y)
        print("\n")
        ax.scatter(x, y)
        ax.annotate(country_name,
                    (x, y),
                    )


    display_axes = fig.add_axes([0.1, 0.1, 0.8, 0.8], projection='polar')
    display_axes._direction = 2*np.pi
    ## This is a nasty hack - using the hidden field to
    ## multiply the values such that 1 become 2*pi
    ## this field is supposed to take values 1 or -1 only!!

    norm = mpl.colors.Normalize(0.0, 2*np.pi)

    # Plot the colorbar onto the polar axis
    # note - use orientation horizontal so that the gradient goes around
    # the wheel rather than centre out
    quant_steps = 2056
    cb = mpl.colorbar.ColorbarBase(display_axes, cmap=cm.get_cmap('hsv',quant_steps),
                                       norm=norm,
                                       orientation='horizontal')



    # aesthetics - get rid of border and axis labels
    cb.outline.set_visible(False)
    display_axes.set_axis_off()
    plt.show()
    # Replace with plt.savefig if you want to save a file

