import csv
import re

outputcsv = csv.writer(open('./output.csv', 'wb'), quoting=csv.QUOTE_ALL)
localcsv = csv.reader(open(r'./dump.csv','r'))
#localcsv.next() #Skip header row

headerrow = ['statefips', 'countyfips', 'countyns10', 'geoid10', 'name', 'namelsad10',
             'boundingbox', 'corner_sw', 'corner_nw', 'corner_ne', 'corner_se', 'corner_wtf', 'extentn', 'extents',
             'extente', 'extentw']
outputcsv.writerow(headerrow)
localcsv.next()

for line in localcsv:
    fml = re.search('(POLYGON\(\()(\S*) (\S*)\,(\S*) (\S*)\,(\S*) (\S*)\,(\S*) (\S*)\,(\S*) (\S*)\)\)$', line[6])    
    tempsw = fml.group(3) + "," + fml.group(2)
    tempnw = fml.group(5) + "," + fml.group(4)
    tempne = fml.group(7) + "," + fml.group(6)
    tempse = fml.group(9) + "," + fml.group(8)
    tempwtf = fml.group(11) + "," + fml.group(10)
    extentw = fml.group(2)
    extents = fml.group(3)
    extentn = fml.group(7)
    extente = fml.group(6)
    line.append(tempsw)
    line.append(tempnw)
    line.append(tempne)
    line.append(tempse)
    line.append(tempwtf)
    line.append(extentn)
    line.append(extents)
    line.append(extente)
    line.append(extentw)
    outputcsv.writerow(line)
"""
    fml = re.search('POLYGON\(\((\S)\ (\S)\,(\S)\ (\S)\,(\S)\ (\S)\,(\S)\ (\S)\,(\S)\ (\S)\)\)', line[6])    
    fml = re.search('(POLYGON\(\()(\S*) (\S*)\,.*$', line[6])    
    print fml[0]
    print fml[1]
    print fml[2]
    print fml[3]
    print fml[4]
    print fml[5]
    print fml[6]
    print fml[7]
"""

