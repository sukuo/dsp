import csv
import pandas as pd
import numpy as np
import re
import pprint
from collections import Counter

fac_cols = ['name', 'degree', 'title', 'email']
fac_table = pd.read_csv('faculty.csv', 
                        names = fac_cols, 
                        header = None, 
                        skiprows = [0] , 
                        skipinitialspace=True)

degree = ' '.join(degree)
degree = degree.split(" ")
degree = [re.sub("Ph\.?D\.?", "PhD", elem) for elem in degree]
degree = [re.sub("Sc\.?D\.?", "ScD", elem) for elem in degree]
freq = Counter(degree)
print(freq)
print('\n')

fac_table['title'] = fac_table['title'].str.replace('As{2}i.+', 'Assistant Professor of Biostatistics')
print(fac_table.groupby('title').count())
print('\n')

emails = fac_table['email'].tolist()
pprint.pprint(emails)
print('\n')
emails = ' '.join(emails)
emails = re.split(("@|\s"), emails )
email_types = [i for i in emails if '.edu' in i]
email_freq = Counter(email_types)
email_freq
