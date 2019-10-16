import pandas as pd
import matplotlib.pyplot as plt

religion_data_filename = "Religion Data.xlsx"

dataframe = pd.read_excel(religion_data_filename)

print(dataframe)


x_axis_name = "Country Religiosity (%)"
y_axis_name = "Research_and_development_spending (% GDP per capita)"

plt.figure()
# dataframe.plot()

