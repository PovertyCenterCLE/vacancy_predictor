import pandas as pd
import csv
import numpy as np
import os

path = '/'.join(os.getcwd().split('/')[:-1])

# get survey data
infile = path+'/data/original_data/main_prop.csv'
outfile = path+'/data/clean_data/main_prop3.csv'

with open(infile, 'r') as fin, open(outfile, 'w') as fout:
    write_to = csv.writer(fout, lineterminator='\n')
    header = next(csv.reader(fin))
    write_to.writerow(header)
    for row in csv.reader(fin):
        if row[1] == "2013":
            write_to.writerow(row)
