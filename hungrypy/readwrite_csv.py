import csv

#opens a csv file called 'data.csv' in read write mode, creates it if it doesnt exist, overwrites it if it exists and stores the instance in csvfile variable
with open("data.csv", "w+") as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(["Col 1", "Col 2"])    #writing first row as a list 
    writer.writerow(["Data 1", "Data 2"])  #2nd row  


#opens data.csv file in readonly mode 
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader: #reading each row and printing it 
        print(row)


#opening an existing file for appending 
with open("data.csv", "a") as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(["Data 3", "Data 4"])



with open("data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile) #DictReader converts it into a dictionary key value pairs: so first row will act as dictionary keys and rest will be their values i.e {'Col 2': 'Data 2', 'Col 1': 'Data 1'}
    for row in reader:
        print(row)


with open("data.csv", "a") as csvfile:
    fieldnames = ["id", "title"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames) #to write as a dictionary
    writer.writerow({"id": 123, "title": "New title"}) #and writing here as a dictionary instead of a list 