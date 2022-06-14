import pandas as pd
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding ='utf-8')
sys.stdout = io.TextIOWrapper(sys.stderr.detach(), encoding ='utf-8')

csv = pd.read_csv('car_num_list2.csv')

count = 1
for index, row in csv.iterrows() :
    print(csv.iloc[index][0][9:22])
    count += 1

print(count)



#print(csv.iloc[0][0][9:24])

# df = pd.DataFrame(csv)

# print(df)

# rows = 11000
# cols = 3
# newdata = [[0 for j in range(cols)] for i in range(rows)]

# answer = ''
# QAcount = 0
# questionMode = True
# indexcount = 0

# print('answer : ' + csv.iloc[0][1])

# for index, row in csv.iterrows() : # csv의 행 만큼 반복
#     if (csv.iloc[index][0] == '답변') :
#         questionMode = False
#         # 첫 열이 답변인 경우 다음 답변이므로, 답변 교체.
#         answer = csv.iloc[index][1]
#         continue
#     elif (csv.iloc[index][0] == '유사질문') :
#         questionMode = True
#         newdata[QAcount][0] = csv.iloc[index][1]
#         newdata[QAcount][1] = answer
#         QAcount = QAcount + 1
#         continue
#     else :
#         if questionMode == True :
#             newdata[QAcount][0] = csv.iloc[index][1]
#             newdata[QAcount][1] = answer
#             QAcount = QAcount + 1
#             continue

# print(newdata, QAcount)

# df = pd.DataFrame(newdata)
# df.to_csv("rectified_jo.csv", header=None, index=None, encoding='utf-8-sig')
#print(len(csv))