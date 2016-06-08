# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>>They both contain sequences of objects separated by commas.  Python lists are contained in brackets [ ] while tuples are contained in parenthesis ( ). The contents of lists are mutable (can be changed) while objects in tuples are immutable.
Keys in a dictionary must be immutable because it would be very difficult to keep track of what these keys are pointing to if they were able to be changed.  Therefore tuples would work as keys to a dictionary.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>>Both contain elements separated by commas and both are mutable.  Sets must have unique elements in it while lists may contain duplicates.  <br />
So for example, if you wanted to compile the first names of everyone on a large sports team, you would use lists because it is somewhat likely that a few of them have the same first names.  Assuming that none of the players have the same exact first and last names, a set would be appropriate to get the names of each unique player. <br />
Performance differs depending on what the user is trying to do.  If you are trying to see if an element is present in a given array, sets are more efficient.  If you are trying to iterate or perform some kind of transformation/function on all of the elements in a given array, then a set would be more efficient.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The `lambda` function is an anonymous function that useful when you only need to call a function once and only once.  Functions are useful because they reduce the amount of code however when a function is used only once, defining a function would actually create more code.  Using a lambda function in these situation makes things cleaner.<br />
For example, if you wanted to classify homes once as ranches or multi-levels in some block of code based on how many floors it has, you could write a lambda function `lambda: "multi-level" if floors > 1 else "ranch"`<br />
For the `key` argument in a `sorted` function, let's say that you had a list of tuples called `pro_players` that looked like:<br />
`(last name, first name, wins, losses, ranking)`<br />
If you wanted to sort by ranking, you would write<br />`sorted(pro_players, key=lambda player: player[4])`


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is an alternative to using lambda functions to define and create lists and uses a linguistic approach instead.  It is also substitute for the `map()` `reduce()` and `filter()` functions.<br />
Suppose you wanted to create a list of cubes called "cbs" using the `map()` function and you had a list of numbers in the range of 0 to 10 called "nums" <br />
`cbs = list(map((lambda x : x**3), nums))`<br />
Filter is similar to the map funtion except it only returns the elements for which the function returns true.  So it would return the same list as "cbs" for a sequence of numbers starting from -10 to 10 if the filter function is defined only for positive numbers.<br />
`map()` is better for creating lists while `filter()` is better for modifying lists.<br />
Set comprehension is very similar to list comprehension except the resulting object is a set.<br />
Dictionary comprehension is also very similar to list comprehension except the code would look like <br />
`dict = {key:value for x in sequence}`


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





