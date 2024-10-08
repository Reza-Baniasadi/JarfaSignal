import csv
import os
import re

def getdatafile(filename):
    array_data = []
    with open(filename,'r' ,newline='', encoding="utf-8")as f:
         filedata = csv.reader(f)
         for row in filedata :
             array_data.append(row)
    return array_data
         

async def CleanGetData(text):
        result = ''
        for horof in text:
            if horof != '*':
                result += horof
        return result

######## this function for get number of file ########
      
def getNumberFile(filevioce,all_voice_data,text):
     if not os.listdir(filevioce):
          with open(f'{filevioce}/0.{text}','a') as f :
               f.write('')

     for file in os.listdir(filevioce):
          file = file.split('.')[0]
          match = re.search(r'(/d+)$',file)  
          if match:
               number = int(match.group(1))
          print(number)
          if os.path.exists(f'{filevioce}/{number}.{text}'):
               continue
          with open(f'{filevioce}/{number}.{text}',"w",encoding='utf-8')as f :
               if text == 'text':
                for onetext in all_voice_data:
                    f.write(onetext)
               elif text == 'ogg':
                         n = number
                         for voice in all_voice_data:
                              with open(f'{filevioce}/{n}.{text}',"wb") as f :
                                   f.write(voice)
                              n += 1