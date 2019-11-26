import csv
import matplotlib.pyplot as plt


def compare_names(str1, str2):
    """Compare two strings alphabetically."""
    if str1 == str2:
        return "identical"
    elif not str1 or not str2:
        return False
    else:
        for index in range(min(len(str1), len(str2))):
            if str1[index] == str2[index]:
                continue
            elif str1[index] < str2[index]:
                return "overpassed"
            else:
                return "searching"


def convert_to_number(str_float):
    """Converts a number retrieved as str from the csv file to float.

    Also does curation of inputs.
    """
    if not str_float:
        return False
    elif str_float[-1] is "%":
        return float(str_float[:-1])
    elif str_float[-1] is "+":
        return float(str_float[:-2])
    else:
        return float(str_float)


def default_plot(x, y, txt, file_name="test.png", annotate=False):
    """Plot the data sets with some default parameters."""
    fig, ax = plt.subplots()
    ax.plot(x, y, 'o')

    plt.xlabel("Country religiosity levels (%)")
    plt.ylabel("Quality of Life Index (a.u.)")

    if annotate:
        for i in range(len(txt)):
            ax.annotate(txt[i], (x[i], y[i]),
                        textcoords="offset points",  # how to position the text
                        xytext=(-10,-10),  # distance from text to points (x,y)
                        ha='left',  # horizontal alignment can be left, right or center
                        )

    fig.savefig(file_name)
    plt.show()


def main(data_file1, data_file2, file_name, annotate=False, to_plot=True):

    # Initialize data storage
    data_countries = list()
    data_religiosity_levels = list()
    data_education_index = list()

    # Open data flesconvert_to_number
    with open(data_file1) as csv_file_1:
        with open(data_file2) as csv_file_2:

            csv_reader_1 = csv.DictReader(csv_file_1, delimiter=',')
            csv_reader_2 = csv.DictReader(csv_file_2, delimiter=',')

            # Read data files line by line
            country_2 = None
            for row_1 in csv_reader_1:
                country_1 = row_1['Country']

                result = compare_names(country_1, country_2)
                print("Step 1: ", country_1, country_2)
                print(result)
                if result == "identical":

                    data_point1 = convert_to_number(row_1["Religion is important"])
                    data_point2 = convert_to_number(row_2["Quality of Life Index"])

                    if data_point1 and data_point2:
                        data_religiosity_levels.append(data_point1)
                        data_education_index.append(data_point2)

                        data_countries.append(row_1["Country"])
                elif result == "overpassed":
                    continue

                for row_2 in csv_reader_2:
                    country_2 = row_2['Country']

                    result = compare_names(country_1, country_2)
                    print("Step 2: ", country_1, country_2)
                    print(result)

                    if result == "identical":

                        data_point1 = convert_to_number(row_1["Religion is important"])
                        data_point2 = convert_to_number(row_2["Quality of Life Index"])

                        if data_point1 and data_point2:
                            data_religiosity_levels.append(data_point1)
                            data_education_index.append(data_point2)

                            data_countries.append(row_1["Country"])
                        break
                    elif result == "overpassed":
                        break

    # Plot
    if to_plot:
        default_plot(data_religiosity_levels, data_education_index, data_countries, file_name=file_name, annotate=annotate)

    print(data_countries)
    print(f"Found {len(data_countries)} matches")


if __name__ == "__main__":
    main('../data/religiosity-levels.csv', '../data/quality-of-life.csv', file_name="../figures/test.png")
