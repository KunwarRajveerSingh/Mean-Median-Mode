import csv
with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)
newdata = []
for i in range(len(filedata)):
    num = filedata[i][1]
    newdata.append(float(num))

n = len(newdata)
newdata.sort()

if n % 2 == 0:
    m1 = float(newdata[n//2])
    m2 = float(newdata[n//2 -1])
    median = (m1 + m2)/2

else:
    median = newdata[n//2]

print("median is:-" + str(median))
    