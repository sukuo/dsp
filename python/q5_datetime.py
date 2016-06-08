# Hint:  use Google to find python function

####a) 
from datetime import datetime

def days_between(d1, d2):
    start = datetime.strptime(d1, '%m-%d-%Y')
    stop = datetime.strptime(d2, '%m-%d-%Y')
    return (stop - start).days
               
date_start = '01-02-2013'
date_stop = '07-28-2015'

delta_days = days_between(date_start, date_stop)
print(delta_days)


####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
