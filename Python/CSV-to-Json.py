#Progam to convert csv to json
import csv
import json

def csv_to_json(csv_file, json_file):
   
    with open(csv_file, mode='r') as file:
#csv.DictReader to read the CSV file as a dictionary 
#Where the keys are the column headers and the values are the corresponding row data.
        reader = csv.DictReader(file)
        print(reader)
        data = list(reader) 
        print(data)    #The entire CSV file is represented as a list of dictionaries

    # Write JSON data to a file
    with open(json_file, mode='w') as file:
        #Converts the list of dictionaries (data) into a JSON formatted string
        json.dump(data, file, indent=2 )


def main():
  csv_file = 'input.csv'
  json_file = 'output.json'
  csv_to_json(csv_file, json_file)

if __name__ == "__main__":
    main()
