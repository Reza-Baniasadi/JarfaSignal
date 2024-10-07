import csv
import asyncio
# def getdatafile(filename):
#     array_data = []
#     with open(filename,'r' ,newline='', encoding="utf-8")as f:
#          filedata = csv.reader(f)
#          for row in filedata :
#              array_data.append(row)
#     return array_data
         

async def CleanGetData(text):
        result = ''
        for horof in text:
            if horof != '*':
                result += horof
        return result
        