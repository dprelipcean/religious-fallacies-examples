import csv
import matplotlib.pyplot as plt


def compare_names(str1, str2):
    """Compare two strings alphabetically."""
    if str1 == str2:
        return "identical"
    else:
        for index in range(min(len(str1), len(str2))):
            if str1[index] == str2[index]:
                continue
            elif str1[index] < str2[index]:
                return "overpassed"
            else:
                return "searching"


def default_plot(x, y, txt, annotate=False):
    fig, ax = plt.subplots()
    ax.plot(x, y, 'o')

    plt.xlabel("Country religiosity levels (%)")
    plt.ylabel("Country Education Index (a.u.)")

    if annotate:
        for i in range(len(txt)):
            ax.annotate(txt[i], (x[i], y[i]),
                        textcoords="offset points",  # how to position the text
                        xytext=(-10,-10),  # distance from text to points (x,y)
                        ha='left',  # horizontal alignment can be left, right or center
                        )

    fig.savefig("figures/test.png")
    plt.show()


def main(data_file1, data_file2, annotate=False):

    # Initialize data storage
    data_countries = list()
    data_religiosity_levels = list()
    data_education_index = list()

    # Open data fles
    with open(data_file1) as csv_file_1:
        with open(data_file2) as csv_file_2:

            csv_reader_1 = csv.DictReader(csv_file_1, delimiter=',')
            csv_reader_2 = csv.DictReader(csv_file_2, delimiter=',')

            # Read data files line by line
            for row_1 in csv_reader_1:
                for row_2 in csv_reader_2:

                    result = compare_names(row_1['Country'], row_2['Country'])

                    if result == "identical":
                        data_countries.append(row_1["Country"])

                        data_religiosity_levels.append(float(row_1["Religion is important"][:-1]))
                        data_education_index.append(float(row_2["EducationIndex"]))
                        continue

                    if result == "overpassed":
                        break

    # Plot
    default_plot(data_religiosity_levels, data_education_index, data_countries)


if __name__ == "__main__":
    main('data/religiosity-levels.csv', 'data/education-index.csv')
