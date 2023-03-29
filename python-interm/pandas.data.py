
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




# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr

dr = cars['drives_right']
# Use dr to subset cars: sel
sel = cars.loc[dr]

# Print sel
print(sel)

# script.py> output:
#          cars_per_cap        country  drives_right
#     US            809  United States          True
#     RU            200         Russia          True
#     MOR            70        Morocco          True
#     EG             45          Egypt          True



# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)