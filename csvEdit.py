import csv
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding ='utf-8')
sys.stdout = io.TextIOWrapper(sys.stderr.detach(), encoding ='utf-8')


csv_file = open("data.csv", "r", encoding='UTF-8-sig')
rdr = csv.reader(csv_file)

for line in rdr :
    print(line[0][1])