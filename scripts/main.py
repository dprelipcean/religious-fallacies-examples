from scripts.congregate_data import congregate_data, extract_data
from scripts.plot import default_plot


def main():
    master_data = congregate_data()
    data_education, data_religion = extract_data(master_data, 'EducationIndex', 'Religion is important')

    print(f'{data_education}{data_religion}')

    default_plot(data_education, data_religion)


if __name__ == "__main__":
    main()
