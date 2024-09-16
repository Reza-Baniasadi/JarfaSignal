import csv


array_data = []

def getdatafile(filename):
    with open(filename,'r')as f:
         filedata = csv.reader(f)
         for row in filedata :
             array_data.append(row)
             return array_data
             
