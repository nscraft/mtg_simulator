import os
import csv

current_script_directory = os.path.dirname(os.path.abspath(__file__))
data_directory = os.path.join(os.path.dirname(current_script_directory), 'Project/Data')
filename = "filename.csv"
fullpath = os.path.join(data_directory, filename)
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

with open(fullpath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print(f"CSV file has been written to {fullpath}")
