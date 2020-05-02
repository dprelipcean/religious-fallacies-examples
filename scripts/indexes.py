indexes_to_compare_with_religiosity_levels = {
    'Education Index': {'horizontal_ticks': (0.3, 1.0, 8)},
    'Expected years of schooling': {'horizontal_ticks': (7, 21, 15)},
    'Mean years of schooling': {'horizontal_ticks': (0, 14, 15)},
    'HDI rank': {'horizontal_ticks': (0, 200, 9)},
    'Happiness Score': {'horizontal_ticks': (0, 8, 17)},
    'GDP per capita': {'horizontal_ticks': (0.3, 1.7, 15)},
    'Social support': {'horizontal_ticks': (0.6, 1.6, 11)},
    'Healthy life expectancy': {'horizontal_ticks': (0.4, 1.2, 9)},
    'Expenditures on R&D (billions of USD)': {'log': True, 'horizontal_ticks': (0.01, 500, 1)},
    'Expenditures on R&D (% of GDP)': {'horizontal_ticks': (0, 5, 11)},
    'Generosity': {'horizontal_ticks': (0, 0.5, 6)},
    'Freedom to make life choices': {'horizontal_ticks': (0, 0.6, 7)},
    'Fight against corruption': {'horizontal_ticks': (0, 0.5, 6)},
}

other_indexes = {
    'Crime vs Religion Diversity Index': {'index': 'Rate', 'index2': 'RDI', 'log': True, 'ylabel': 'Criminality rate', 'xlabel': 'Religious Diversity Index', 'plot_regression': False, 'horizontal_ticks': (0, 10, 11), 'zoom_factor': 3}
}
