# Lab 9.10
# Linh Pham - ID# 2027194
# This program reads in the name of an input file and then reads the file using the csv.reader() method.

import csv
filename = input()
output = open(filename)
data = csv.reader(output, delimiter=',')
words = []
for row in data:
    for word in row:
        words.append(word.strip())

for i in range(len(words)):
    if words[i] not in words[:i]:
        count = 0
        for w in words:
            if words[i] == w:
                count += 1
        print(words[i], count)
output.close()
