import pandas as pd
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding ='utf-8')
sys.stdout = io.TextIOWrapper(sys.stderr.detach(), encoding ='utf-8')

csv = pd.read_csv('C:/Users/MJ/Desktop/pythonWorkspace/rectified.csv')

count = 0
for index, row in csv.iterrows() : # csv의 행 만큼 반복
    if '질문' in csv.iloc[index][1] :
        count = count + 1
        print(index+2)

print('총 개수 :', count)