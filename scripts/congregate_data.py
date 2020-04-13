import csv

data_location = '../data/'
data_files = {'education-index.csv': ['EducationIndex', 'Expected years of schooling', 'Mean years of schooling', 'HDI rank'],
              'religiosity-levels.csv': ['Religion is important', 'Religion is unimportant'],
              'happiness-index.csv': ['Happiness Score', 'GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'],
              'research.csv': ['Expenditures on R&D (billions of USD)', '% of GDP']}


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
