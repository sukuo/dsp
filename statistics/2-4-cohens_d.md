[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> firsts = df[df.birthord==1]</br>
others = df[df.birthord>1]</br>
first_mean = firsts.totalwgt_lb.mean()</br>
others_mean = others.totalwgt_lb.mean()</br>
var_first = firsts.totalwgt_lb.var()</br>
var_others = others.totalwgt_lb.var()</br>
pooled_var = (len(firsts)*var_first + len(others)*var_others) / (len(firsts)+len(others))</br>

>>def cohen_d(mean1, mean2, pv):</br>
    return (abs(mean1 - mean2) / pv)</br>

>>ex2_4 = cohen_d(first_mean, others_mean, pooled_var)</br>
print("Cohen's D =", round(ex2_4, 4))

**__Cohen's D = 0.063__**

