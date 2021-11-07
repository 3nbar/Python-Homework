import pandas as pd
from os import walk
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook



def creatXlsx(path, df):
    with pd.ExcelWriter(path) as writer:
        df.to_excel(writer, sheet_name='sheet1')

def insertData(studentNum, studentName):

    f = []
    for (dirpath, dirnames, filenames) in walk('file'):
        f.extend(filenames)
        break
    path = 'file/file.xlsx'


    if 'file.xlsx' in f:
        df = pd.read_excel(open('file/file.xlsx', 'rb'),sheet_name='sheet1') 
        df =df[['studentNumber','studentName','score']]
        state = 0
        for ind in df.index:
            if df.loc[ind,'studentNumber'] == studentNum:
                if df.loc[ind,'studentName'] == studentName:
                    print('exist')
                    state = 1
                
        if state==0:
            df2 = pd.DataFrame([[studentNum, studentName,'']], index=[df.index.stop], columns=['studentNumber', 'studentName', 'score'])
            df = df.append(df2)
            creatXlsx(path, df)
            print('done')
        
        
    else:
        df = pd.DataFrame([[studentNum, studentName,'']], index=[1], columns=['studentNumber', 'studentName', 'score'])
        creatXlsx(path, df)  
    


insertData(1111,"ali")
insertData(2222,"alihh")
insertData(3333,"ali33")
insertData(4444,"ali34")
insertData(5555,"ali343")
insertData(6666,"ali")




