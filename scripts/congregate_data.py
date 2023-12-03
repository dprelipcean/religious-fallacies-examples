from pandas import DataFrame, read_csv, concat

import csv

data_location = '../data/'

metadata_country = {
    "metadata_country.csv": ["Continent"],
}

data_files = {
    'education-index.csv': ['Education Index', 'Expected years of schooling', 'Mean years of schooling', 'HDI rank'],
    'religiosity-levels.csv': ['Religion is important', 'Religion is unimportant'],
    'happiness-index.csv': ['Happiness Score', 'GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Fight against corruption'],
    'research.csv': ['Expenditures on R&D (billions of USD)', 'Expenditures on R&D (% of GDP)'],
    'religious-diversity-index.csv': ['RDI'],
    'crime-rate.csv': ['Rate']
}


def congregate_data():
    master_data = dict()
    for data_file_name in data_files.keys():
        with open(f'{data_location}{data_file_name}') as csv_file:
            csv_reader_1 = csv.DictReader(csv_file, delimiter=',')

            for row in csv_reader_1:
                for index in data_files[data_file_name]:
                    country = row['Country']
                    value = row[index]
                    # print(country)

                    if country not in master_data.keys():
                        master_data[country] = dict()

                    if value == 'n.a.':
                        continue
                    elif value:
                        try:
                            master_data[country][index] = float(value)
                        except ValueError:
                            master_data[country][index] = float(value[:-1])

    return master_data


def extract_data(dictionary, key_1, key_2):
    countries = dictionary.keys()

    data_extracted_1 = list()
    data_extracted_2 = list()
    data_countries = list()

    for country in countries:
        if (key_1 in dictionary[country].keys()) and (key_2 in dictionary[country].keys()):
            data_extracted_1.append(dictionary[country][key_1])
            data_extracted_2.append(dictionary[country][key_2])
            data_countries.append(country)

    return data_extracted_1, data_extracted_2, data_countries


def extract_data_dataframe(dataframe, key_1, key_2, year=2022):
    data_countries = dataframe.index.to_list()
    data_continent = dataframe["Continent"].to_list()
    data_population = dataframe[f"{year}"].to_list()

    data_extracted_1 = dataframe[key_1].to_list()
    data_extracted_2 = dataframe[key_2].to_list()

    return data_extracted_1, data_extracted_2, data_countries, data_continent, data_population


def congregate_data_full():
    master_data = dict()
    for data_file_name in data_files.keys():
        with open(f'{data_location}{data_file_name}') as csv_file:
            csv_reader_1 = csv.DictReader(csv_file, delimiter=',')

            for row in csv_reader_1:
                for index in data_files[data_file_name]:
                    country = row['Country']
                    value = row[index]
                    # print(country)

                    if country not in master_data.keys():
                        master_data[country] = dict()

                    if value == 'n.a.':
                        continue
                    elif value:
                        try:
                            master_data[country][index] = float(value)
                        except ValueError:
                            master_data[country][index] = float(value[:-1])

    master_data_dataframe = DataFrame.from_dict(master_data, orient="index")
    # print(master_data_dataframe)

    metadata_country_continent_filename = "../metadata_country/continents-according-to-our-world-in-data.csv"
    metadata_country_continent_dataframe = read_csv(metadata_country_continent_filename, index_col="Entity")
    # print(metadata_country_continent_dataframe)

    metadata_country_population_filename = "../metadata_country/population.csv"
    metadata_country_population_dataframe = read_csv(metadata_country_population_filename, index_col="Country")
    # print(metadata_country_population_dataframe)

    # Axis 1 merges the identical rows
    master_data = concat([metadata_country_continent_dataframe,
                          metadata_country_population_dataframe,
                          master_data_dataframe],
                         axis=1)
    # print(master_data)

    return master_data


if __name__ == '__main__':
    master_data = congregate_data_full()

    selection = master_data.loc[master_data["Continent"] == "Europe"]
    # print(selection["Expenditures on R&D (% of GDP)"])

