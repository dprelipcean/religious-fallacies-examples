from core.congregate_data import congregate_data, congregate_data_full
from core.indexes import indexes_to_compare_with_religiosity_levels, other_indexes
from core.plot import plot_per_continent, plot_color_scheme


def main():
    master_data = congregate_data_full()

    plot_color_scheme(master_data)

    # for index, kwargs in indexes_to_compare_with_religiosity_levels.items():
    #     plot_per_continent(master_data, index=index, **kwargs)
    #
    # for analysis, kwargs in other_indexes.items():
    #     plot_per_continent(master_data, name=analysis, **kwargs)


if __name__ == "__main__":
    main()
