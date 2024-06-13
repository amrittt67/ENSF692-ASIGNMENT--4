# calgary_dogs.py
# AMRIT KAUR
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import pandas as pd
import numpy as np

def main():

    # Import data here
    dataFrame = pd.read_excel('CalgaryDogBreeds.xlsx', engine='openpyxl')
    print("ENSF 692 Dogs of Calgary")

    # User input stage
    while True:
        breed = input('Please enter a dog breed: ')
    
        if breed.title() in dataFrame['Breed'].str.title().unique():
            break
        else:
            print("Dog breed not found in the data. Please try again.")

    breed = breed.upper()
        
        
    # Data anaylsis stage
    data = dataFrame[dataFrame['Breed'] == breed]
    
    # Print all years where listed breed was top
    dataYears = data['Year'].unique()
    print(f'The {breed} was found in the top breeds for years: ', end='')
    for year in dataYears:
        print(year, end=' ')
    print('')
    
    
    # Total registrations
    registrations = data['Total'].sum()
    print(f'There have been {registrations} {breed.upper()} dogs registered total.')

    # Registrations per year
    for year in data['Year'].unique():
        data_year = data[data['Year'] == year]
        percent = (data_year['Total'].sum() / dataFrame.loc[dataFrame['Year'] == year]['Total'].sum()) * 100
        print(f'The {breed.upper()} was {percent}% of top breeds in {year}')

    # Total Percentage
    totalPercentage = (registrations / dataFrame['Total'].sum()) * 100
    print(f'The {breed.upper()} was {totalPercentage} of top breeds across all years.')
 
    #Most popular month
    months = data.groupby('Month')['Total'].sum()
    max_registrations = np.max(months)
    max_months = months[months == max_registrations].index
    print(f'Most popular month(s) for {breed.upper()}: ', end = "")
    print(*max_months)

    
if __name__ == '__main__':
    main()

