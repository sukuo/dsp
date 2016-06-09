#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv
from operator import itemgetter

def read_data(data):
  football_csv = open(data, 'r')
  football_data = csv.reader(football_csv)
  football_list = list(football_data)
  return football_list

def get_min_score(parsed_data):
    diff_list = []
    i = 1
    while i < len(read_data('football.csv')):
        diff = abs(int(parsed_data[i][5]) - int(parsed_data[i][6]))
        diff_list.append(diff)
        i+=1
    return min(diff_list)

print("Minimum difference in PF and PA is", +get_min_score(read_data('football.csv')))

def get_team(parsed_data):
    diff_list = []
    i = 1
    while i < len(read_data('football.csv')):
        diff = abs(int(parsed_data[i][5]) - int(parsed_data[i][6]))
        diff_list.append([parsed_data[i][0], diff])
        i+=1
    sorted_list = sorted(diff_list, key = itemgetter(1))
    return sorted_list[0][0]

print("The team with the smallest differential is"+" "+get_team(read_data('football.csv')))
