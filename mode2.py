from collections import Counter
import csv
import statistics

with open("MMMR.csv",newline="") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

newData = []

for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append(float(num))

n = len(newData)
data = Counter(newData)
getMode = dict(data)
mode = []
mode1 = []
mode2 = []

for a,v in getMode.items():
    a = float(a)
    if(50<a<60):
        if(v == max(list(data.values()))):
            mode.append(a)
    elif(60<a<70):
        if(v == max(list(data.values()))):
            mode1.append(a)
    elif(70<a<75):
        if(v == max(list(data.values()))):
            mode2.append(a)

if(len(mode)>len(mode1) and len(mode2)):
    print(mode)
elif(len(mode1)>len(mode) and len(mode2)):
    print(mode1)
elif(len(mode2)>len(mode) and len(mode1)):
    print(mode2)