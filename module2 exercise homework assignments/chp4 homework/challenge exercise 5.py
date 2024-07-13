## Author: Francisco Bumanglag
## Project: Average Rainfall 
## Assignment: Module 2 Project 2
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: June 24, 2023


#user enters the number of years 
years = int(input('Enter the number of years: '))

#declare variables
total_rainfall = 0
num_years = years

#nested for loop to iterate over years and months
for year in range(1, num_years + 1):
    for month in range(1, 13):              

        rainfall = float(input("Enter the inches of rainfall for Year {}: ".format(year,month)))
        total_rainfall += rainfall 

#after loop, calc average -- total rainfull / months
average_rainfall = total_rainfall / month

#print function - display output
print("Number of months:", month)
print("Total Inches of rainfall:", total_rainfall)
print("Total average rainfall per month:", average_rainfall)





