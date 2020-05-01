from scripts.plotting_scripts import default_plot_function, plot_education_index_function
from numpy import linspace

index_dict = {
    'Education Index': {'plot_function': plot_education_index_function, 'horizontal_ticks': (0.3, 1.0, 8)},
    'Expected years of schooling': {'plot_function': default_plot_function, 'horizontal_ticks': (7, 21, 15)},
    'Mean years of schooling': {'plot_function': default_plot_function, 'horizontal_ticks': (0, 14, 15)},
    'HDI rank': {'plot_function': default_plot_function, 'horizontal_ticks': (0, 200, 9)},
    'Happiness Score': {'plot_function': default_plot_function, 'horizontal_ticks': (0, 8, 17)},
    'GDP per capita': {'plot_function': default_plot_function, 'horizontal_ticks': (0.3, 1.7, 15)},
    'Social support': {'plot_function': default_plot_function, 'horizontal_ticks': (0.6, 1.6, 11)},
    'Healthy life expectancy': {'plot_function': default_plot_function, 'horizontal_ticks': (0.4, 1.2, 9)},
    'Expenditures on R&D (billions of USD)': {'plot_function': default_plot_function, 'log': True, 'horizontal_ticks': (0.01, 500, 1)},
    'Expenditures on R&D (% of GDP)': {'plot_function': default_plot_function, 'horizontal_ticks': (0, 5, 11)},
    'Generosity': {'plot_function': default_plot_function, 'horizontal_ticks': (0, 0.5, 6)},
    'Freedom to make life choices': {'plot_function': default_plot_function, 'horizontal_ticks': (0, 0.6, 7)},
    'Fight against corruption': {'plot_function': default_plot_function, 'horizontal_ticks': (0, 0.5, 6)}
}
