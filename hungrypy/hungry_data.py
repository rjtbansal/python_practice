import csv
import datetime
import shutil 
from tempfile import NamedTemporaryFile

def get_length(file_path): #for auto increment
    with open("data.csv","r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader) #getting reader object as a list of rows 
        return len(reader_list) #reader_list length will give us the row length

def append_data(file_path, name, email, amount):
    fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date'] #these will be the header fieldnames
    #the number of rows? 
    next_id = get_length(file_path) #getting the incremented value for new role 
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
                "id": next_id,
                "name": name,
                "email": email,
                "amount":amount,
                "sent":"",
                "date":datetime.datetime.now()
            })

append_data("data.csv", "Rajat", "rajat@gmail.com", 123.32)

#way we edit data is we copy all data in temp file and append to that temp file 
#eventually we copy everything to the main file by overwriting it
def edit_data(edit_id=None, email=None, amount=None, sent=None):
    filename = "data.csv"
    temp_file = NamedTemporaryFile(delete=False)  #creating a temporary file, delete=False ensures file isnt deleted after writing

    with open(filename, "rb") as csvfile, temp_file: #reading file in binary mode and saving in csvfile and temp_file variables
        reader = csv.DictReader(csvfile) #reading as dict from original csv file 
        fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames) #writing to temp_file
        writer.writeheader()
        for row in reader:
            #print(row['id'] == 4)
            if edit_id is not None: #if edit_id specified
                if int(row['id']) == int(edit_id): #if id matches
                    row['amount'] = amount
                    row['sent'] = sent
            elif email is not None and edit_id is None:
                if str(row['email']) == str(email):
                    row['amount'] = amount
                    row['sent'] = sent
            else:
                pass
            writer.writerow(row) #write the specific row 
        
        shutil.move(temp_file.name, filename) #moving data from temp_file to original file 
        return True
    return False
edit_data(email='rajat@gmail.com',amount=300, sent='')