import csv

def get_length(file_path): #for auto increment
    with open("data.csv") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader) #getting reader object as a list of rows 
        print(reader_list)
        return len(reader_list) #reader_list length will give us the row length

def append_data(file_path, name, email):
    fieldnames = ['id', 'name', 'email'] #these will be the header fieldnames
    #the number of rows? 
    next_id = get_length(file_path) #getting the incremented value for new role 
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
                "id": next_id,
                "name": name,
                "email": email,
            })

append_data("data.csv", "Rajat", "rajat@gmail.com")