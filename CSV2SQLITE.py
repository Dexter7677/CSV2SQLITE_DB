import csv

file = open("/Users/deepakkumarsingh/Documents/test.csv","r")
reader = csv.reader(file)

rownum = 0
colnum = 0
for row in reader:
# Save header row.
    if rownum ==0:
        header = row
    else:
        colnum = 0
    for col in row:
        print ('%-8s: %s' % (header[colnum], col))
        colnum += 1
 
    rownum += 1
 
file.close()