
# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame

print(cars[['country']])
# Print out DataFrame with country and drives_right columns
print(cars.loc[:, ['country', 'drives_right']])



# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan

print(cars.iloc[2])
# Print out observations for Australia and Egypt

print(cars.loc[['AUS','EG']])

# <script.py> output:
#     cars_per_cap      588
#     country         Japan
#     drives_right    False
#     Name: JPN, dtype: object
#          cars_per_cap    country  drives_right
#     AUS           731  Australia         False
#     EG             45      Egypt          True