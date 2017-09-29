#Name: Lilian Sheu
#Discussion: Thursdays 3-4 pm

import os
import filecmp
import sys
import csv
from collections import OrderedDict
import time
import datetime

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	f = open(file, "r")
	f.readline() #skip first line
	list_of_files = []
	for row in f:
		dict_file = {}
		split_list = row.split(',')
		dict_file['First'] = split_list[0]
		dict_file['Last'] = split_list[1]
		dict_file['Email'] = split_list[2]
		dict_file['Class'] = split_list[3]
		dict_file['DOB'] = split_list[4].split('\n')[0]
		list_of_files.append(dict_file)
	return list_of_files

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	col = str(col)
	newlist = sorted(data, key=lambda k:k[col])
	returned_list = [newlist[0]['First'], newlist[0]['Last']]
	final_sort = ' '.join(returned_list)
	return final_sort

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	size_senior = 0
	size_junior = 0
	size_fresh = 0
	size_soph = 0
	for d in data:
		if d['Class'] == 'Senior':
			size_senior += 1
		elif d['Class'] == 'Junior':
			size_junior += 1
		elif d['Class'] == 'Freshman':
			size_fresh += 1
		else:
			size_soph += 1
	class_list = []
	class_list.append(('Senior', size_senior))
	class_list.append(('Junior', size_junior))
	class_list.append(('Freshman', size_fresh))
	class_list.append(('Sophomore', size_soph))
	sorted_class_list = sorted(class_list, key=lambda t:t[1], reverse=True)
	return sorted_class_list


# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	day_count = {}
	for d in a:
		for x in d:
			if x == 'DOB':
				if d[x][1] == '/':
					if d[x][3] == '/':
						if d[x][2] in day_count:
							day_count[d[x][2]] += 1
						else:
							day_count[d[x][2]] = 1
					else:
						if d[x][2:4] in day_count:
							day_count[d[x][2:4]] += 1
						else:
							day_count[d[x][2:4]] = 1
				else:
					if d[x][4] == '/':
						if d[x][3] in day_count:
							day_count[d[x][3]] += 1
						else:
							day_count[d[x][3]] = 1
					else:		
						if d[x][3:5] in day_count:
							day_count[d[x][3:5]] += 1
						else:
							day_count[d[x][3:5]] = 1
	most_seen_day = 0
	new_num = 0
	for count in day_count:
		if day_count[count] > most_seen_day:
			most_seen_day = day_count[count]
			new_num = int(count)

	return new_num


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest 
# integer.  You will need to work with the DOB to find their current age.


	#Your code here:
	today_date = time.strftime('%m/%d/%Y').split('/')
	list_ages = []
	for d in a:
		for x in d:
			if x == 'DOB':
				list_DOB = d[x].split('/')
				temp_age = int(today_date[2])-int(list_DOB[2])
				list_ages.append(temp_age)
	avg_age = sum(list_ages)/len(list_ages)

	if (sum(list_ages)%len(list_ages)) < 5:
		return round(avg_age)
	else:
		return round(avg_age)


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	f = open(fileName, 'w', newline='\n')
	col = str(col)
	newlist = sorted(a, key=lambda k:k[col])
	wanted_keys = ['First', 'Last', 'Email']
	newer_list = []
	for x in newlist:
		empty_dict = {}
		for y in x:
			if y not in wanted_keys:
				continue
			else:
				empty_dict[y] = x[y]
		newer_list.append(empty_dict)
	with f as fileName:
		dict_writer = csv.DictWriter(fileName, wanted_keys)
		dict_writer.writerows(newer_list)



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

