import csv 
import math

with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
data = file_data[0]
total = 0

print(data)

for integers in file_data:
    total += float(integers[1])

total = 0
n = len(file_data)

mean = total/n

squaredlist = []
for number in file_data:
    a = float(number) - float(mean)
    print(a)
    a = a**2 
    squaredlist.append(a)

sum = 0
for i in squaredlist:
    sum = sum+i

result = sum/n-1

Stdvtn = math.sqrt(result)

print(Stdvtn)