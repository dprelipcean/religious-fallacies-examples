from scripts.congregate_data import congregate_data
from scripts.indexes import indexes_to_compare_with_religiosity_levels, other_indexes
from scripts.plot import default_plot


def main():
    master_data = congregate_data()

    # for index, kwargs in indexes_to_compare_with_religiosity_levels.items():
    #     default_plot(master_data, index=index, **kwargs)

    for analysis, kwargs in other_indexes.items():
        default_plot(master_data, name=analysis, **kwargs)


if __name__ == "__main__":
    main()
