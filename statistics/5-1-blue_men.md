[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> import scipy<br/>
<br/>
def feet_cm(height):<br/>
    height = height.split("'")<br/>
    inches = (int(height[0]) * 12) + int(height[1])<br/>
    cents = inches * 2.54<br/>
    return cents<br/>
<br/>
m_lower = "5'10"<br/>
m_upper = "6'1"<br/>
params = scipy.stats.norm(loc = 178, scale = 7.7)<br/>
perc_in_range = params.cdf(feet_cm(m_upper)) - params.cdf(feet_cm(m_lower))<br/>
print("The percentage of males between 5'10 and 6'1 is approximately", round(perc_in_range, 3)*100,"%")<br/>

***___The percentage of males between 5'10 and 6'1 is approximately 34.3 %___***
