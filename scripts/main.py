from scripts.congregate_data import congregate_data
from scripts.plot import plot_education_index, default_plot, plot_research_expenditure_absolute, plot_research_expenditure_relative


def main():
    master_data = congregate_data()
    index_list = ['Happiness Score', 'Generosity', 'Freedom to make life choices', 'Perceptions of corruption']

    # plot_education_index(master_data)
    # plot_research_expenditure_absolute(master_data)
    # plot_research_expenditure_relative(master_data)

    for index in index_list:
        default_plot(master_data, index)


if __name__ == "__main__":
    main()
