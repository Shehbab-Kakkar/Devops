#Progam to convert JSON to CSV
import json
import csv

def json_to_csv(json_file, csv_file):
    # Read the JSON file
  with open(json_file, mode='r') as file:
    data = json.load(file)
    print(data)
    
# Get the keys for the CSV header from the first dictionary in the JSON data
  header = data[0].keys()
  print(header)
  # Write CSV data to the file
  with open(csv_file, mode='w', newline='') as file:
  #The csv.DictWriter() method will write to a CSV file 
  #using rows of data that are already formatted as dictionaries.
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()   # writes the header row to the CSV file.
    writer.writerows(data)
    #writes the rows of data from the list of dictionaries to the CSV file.

def main():
    json_file = 'input.json'  # Input JSON file
    csv_file = 'output.csv'  # Output CSV file
    json_to_csv(json_file, csv_file)

if __name__ == "__main__":
    main()


