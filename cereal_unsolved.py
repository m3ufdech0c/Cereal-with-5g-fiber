import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal.csv")

#open and read csv
with open(cereal_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first ()
    # `csv.reader` begins reading the CSV file from the first row. `next(csv_reader, None)` will skip the header row.
    csv_header = next(csvfile)
    print(f"Header: {csvfile}")

    #Read through each row of data after the header
    for row in csvreader:

        #Convert row to float and compare to grams of fiber
        if float(row[7]) >= 5:
            print(row)