[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> #Stats question 3.1a</br>
</br>
import chap01soln</br>
import numpy as np</br>
import matplotlib.pyplot as plt</br>
</br>
resp = chap01soln.ReadFemResp()</br>
a = resp.numkdhh</br>
val, cnt = np.unique(a, return_counts=True)</br>
probs = cnt / len(a)</br>
width=1</br>
print("Mean of unbiased =", np.mean(a))</br>
plt.bar(val, probs, width)</br>
plt.show</br>
__Mean of unbiased = 1.024205155043831__


</br>
</br>
>>>#Stats question 3.1b</br>
</br>
import chap01soln</br>
import numpy as np</br>
import matplotlib.pyplot as plt</br>
</br>
resp = chap01soln.ReadFemResp()</br>
a = resp.numkdhh</br>
val, cnt = np.unique(a, return_counts=True)</br>
probs = cnt / len(a)</br>
biased_freq = [[val[i], (val[i]*cnt[i])/total] for i in range(len(val))]</br>
biased_probs = [biased_freq[i][1] for i in range(len(biased_freq))]</br>
width=1</br>
"""There seems to be some rounding error compared to the textbook \
answers or some other underlying issue with my code"""</br>
average = [val[i]*biased_probs[i] for i in range(len(val))]</br>
print("Average of biased distribution is", sum(average))</br>
plt.bar(val, biased_probs, width)</br>
plt.show</br>
__Mean of biased = 2.46186052597__


