from scripts.congregate_data import congregate_data
from scripts.indexes import index_dict
from scripts.plot import default_plot


def main():
    master_data = congregate_data()

    for index, kwargs in index_dict.items():
        default_plot(master_data, index=index, **kwargs)


if __name__ == "__main__":
    main()
