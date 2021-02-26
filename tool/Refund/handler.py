import pandas as pd
import os
import time

dir = 'refund data/'
list_of_file = [fn for fn in os.listdir(dir)]

print(list_of_file)

with open('import this to excel.txt', 'w') as w:
    for i in range(len(list_of_file)):
        file = list_of_file[i]
        with open(dir + file, 'r') as r:
            line = r.readlines()
            r.close()

        sub_line = line[3:-1]
        for i in range(len(sub_line)):
            sub_line[i] = sub_line[i].replace('|', '\t')
            print(sub_line[i])
            w.write('{}'.format(sub_line[i]))

    w.close()

