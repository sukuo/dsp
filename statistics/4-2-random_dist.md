[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>>**PMF of randomly drawn numbers**</br>
</br>
import numpy as np</br>
import matplotlib.pyplot as plt</br>
</br>
rand_array = np.random.random_sample((1000,))</br>
bins = np.linspace(0, 1, 50)</br>
plt.hist(rand_array, bins)</br>
plt.show()</br>
</br>
___


>>**CDF of randomly drawn numbers**</br>
</br>
import matplotlib.pyplot as plt</br>
</br>
n_bins = 100</br>
n, bins, patches = plt.hist(rand_array, n_bins, normed=1, </br>
                            histtype='step', cumulative=True)</br>
</br>
>>>The randomly drawn numbers do not appear to be completely random.  While the PMF may not perfectly show that it is drawn from a uniform distribution, with a larger sample size it will approach the shape of the uniform distribution.</br>
The CDF does a better job at showing that the "randomly" drawn numbers are from a uniform distribution because the pattern that appears is approximately a straight line indicating the numbers were drawn from a uniform distribution. 
