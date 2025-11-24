import csv

inventory = []

def read():
    with open('data_inventory.csv', mode='r', newline='') as file_csv:
        read_csv = csv.reader(file_csv)
        for fila in read_csv:
            print(fila)

def write():
    with open('data_inventory.csv', mode='w', newline='') as file_csv:
        write_csv = csv.writer(file_csv)

        write_csv.writerow(["name","Price","Quantity"])
        write_csv.writerows(inventory)