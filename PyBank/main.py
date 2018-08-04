#Initiate Dependencies
import csv
import os

#Specify the file
file = 'C:\\Users\\Kat\\Dropbox\\Work\\Data Boot Camp\\HW\\python_challenge\\PyBank\\Resources\\budget_data.csv'
#file = os.path.join('Resources','budget_data.csv')

#Open the file to be read and set the contents to list
with open(file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    budget_list = list(csvreader)

#Count the number of rows in list to get total months
#Sum the values in second column to get total profits

month = 0
total = 0
    
month = sum(1 for row in budget_list)
    
total = sum(int(row[1]) for row in budget_list)

#Create a new list including only the Profits/Losses
budgets = []
for row in budget_list:
    budgets.append(int(row[1]))

#Create a new list using budgets list that takes the difference between the value two rows
diff = [j-i for i, j in zip(budgets[:-1], budgets[1:])]

#Sum the diff list and then divide by number of values in list to get average Profits/Losses
avg_change = round(sum(diff) / float(len(diff)),2)

#Append the diff list with 0 for the first value
difflist = [0]
difflist = difflist + diff

#Find the index of the max value in the diff list
max_prof = max(difflist)
max_pos = difflist.index(max(difflist))

#Find the index of the min value in the diff list
min_prof = min(difflist)
min_pos = difflist.index(min(difflist))

#Print the findings
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {month}")
print(f"Total: {total}")
print(f"Average change: ${avg_change}")
print(f"Greatest increase in profits: {budget_list[max_pos][0]} (${difflist[max_pos]})")
print(f"Greatest decrease in profits: {budget_list[min_pos][0]} (${difflist[min_pos]})")