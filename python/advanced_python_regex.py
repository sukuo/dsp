PART1 

Q1
import csv
import pandas as pd
import numpy as np
import re
from collections import Counter

degrees = []
fac_cols = ['name', 'degree', 'title', 'email']
fac_table = pd.read_csv('faculty.csv', 
                        names = fac_cols, 
                        header = None, 
                        skiprows = [0] , 
                        skipinitialspace=True)

degree = ' '.join(degree)
degree = degree.split(" ")

degree1 = [re.sub("Ph\.?D\.?", "PhD", elem) for elem in degree]
degree2 = [re.sub("Sc\.?D\.?", "ScD", elem) for elem in degree1]

freq = Counter(degree2)
print(freq)

fac_table['title'] = fac_table['title'].str.replace('As{2}i.+', 'Assistant Professor of Biostatistics')
fac_table.groupby('title').count()
