import csv
import pandas as pd
import numpy as np



fac_cols = ['name', 'degree', 'title', 'email']
fac_table = pd.read_csv('faculty.csv', 
                        names = fac_cols, 
                        header = None, 
                        skiprows = [0] , 
                        skipinitialspace=True)

email = fac_table['email']
email.to_csv('UPenn_emails.csv', index = False, header = False)
