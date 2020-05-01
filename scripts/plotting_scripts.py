colors = {'blue': '#2300A8', 'yellow': '#FFFF00', 'green': '#00A658', 'red': '#FF0000'}


def default_plot_function(ax, data_religion_level, data_index):
    ax.plot(data_religion_level, data_index, 'o', color=colors['blue'])


def plot_education_index_function(ax, data_religion_level, data_index):

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
