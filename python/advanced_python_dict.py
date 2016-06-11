import csv
import pandas as pd
import numpy as np
import re
import pprint
from collections import defaultdict
from itertools import islice


fac_cols = ['name', 'degree', 'title', 'email']
fac_table = pd.read_csv('faculty.csv', 
                        names = fac_cols, 
                        header = None, 
                        skiprows = [0] , 
                        skipinitialspace=True)

degree = fac_table['degree']
degree = [re.sub("Ph\.?D\.?", "PhD", elem) for elem in degree]
degree = [re.sub("Sc\.?D\.?", "ScD", elem) for elem in degree]

fac_table['title'] = fac_table['title'].str.replace('As{2}i.+', 'Assistant Professor of Biostatistics')
title = fac_table['title'].tolist()

emails = fac_table['email'].tolist()

names = fac_table['name']
split_names = [i.split(" ") for i in names]
last_names = [i[-1] for i in split_names]
first_middle = []
for i in split_names:
    if len(i) == 2:
        first_middle.append((i[0]))
    else:
        first_middle.append(i[0]+" "+i[1])

dict_vals = [[degree[i], title[i], emails[i]] for i in range(len(emails))]
faculty_dict = defaultdict(list)

for i in range(len(last_names)):
    faculty_dict[last_names[i]].append(dict_vals[i])

pairs = []
for k,v in faculty_dict.items():
    pairs.append((k,v))
pprint.pprint(pairs[:3])
print('\n')

profs = []
full_names = [(first_middle[i], last_names[i]) for i in range((len(last_names)))]
professor_dict = dict(zip(full_names, dict_vals))

for k,v in professor_dict.items():
    profs.append((k,v))
pprint.pprint(profs[:3])
print('\n')
pprint.pprint(sorted(profs, key=lambda profs: profs[0][1])[:3])
