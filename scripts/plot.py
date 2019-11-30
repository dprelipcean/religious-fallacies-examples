import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


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


def extract_name_from_file(filename):
    """Extract a name from the filename."""
    return filename[8:-4]


def default_plot(x, y, txt, regression_x=None, regression_y=None, file_name="test.png", annotate=False, ylabel=None):
    """Plot the data sets with some default parameters."""
    fig, ax = plt.subplots()
    ax.plot(x, y, 'o')

    plt.xlabel("Country religiosity levels (%)")
    plt.ylabel(f"{ylabel} (a.u.)")

    if annotate:
        for i in range(len(txt)):
            ax.annotate(txt[i], (x[i], y[i]),
                        textcoords="offset points",  # how to position the text
                        xytext=(-10, -10),  # distance from text to points (x,y)
                        ha='left',  # horizontal alignment can be left, right or center
                        )

    plt.plot(regression_x, regression_y, '-r')
    ax.legend(['Data Points', 'Regression Line'])

    fig.savefig(file_name)
    plt.show()


def regression_points(x, y):
    """Find regression line"""
    gradient, intercept, r_value, p_value, std_err = linregress(x, y)
    mn = np.min(x)
    mx = np.max(x)
    x1 = np.linspace(mn, mx, 500)
    y1 = gradient * x1 + intercept
    return x1, y1


def main(data_file1, data_file2, file_name, annotate=False, to_plot=True, data_feature=None):

    # Initialize data storage
    data_countries = list()
    data_religiosity_levels = list()
    data_education_index = list()

    # Open data and convert_to_number
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
                    data_point2 = convert_to_number(row_2[data_feature])

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
                        data_point2 = convert_to_number(row_2[data_feature])

                        if data_point1 and data_point2:
                            data_religiosity_levels.append(data_point1)
                            data_education_index.append(data_point2)

                            data_countries.append(row_1["Country"])
                        break
                    elif result == "overpassed":
                        break

    # Find regression lines
    x, y = regression_points(data_religiosity_levels, data_education_index)

    # Plot
    ylabel = extract_name_from_file(data_file2)
    if to_plot:
        default_plot(data_religiosity_levels, data_education_index, data_countries,
                     regression_x=x, regression_y=y,
                     file_name=file_name, annotate=annotate, ylabel=ylabel)

    print(data_countries)
    print(f"Found {len(data_countries)} matches")


if __name__ == "__main__":
    main('../data/religiosity-levels.csv', '../data/Happiness-index.csv',
         data_feature='Score',
         file_name="../figures/happiness-index.png")
