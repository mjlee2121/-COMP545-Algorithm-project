import calendar
from datetime import date
import holidays
import csv
import pandas as pd
from io import StringIO

df = pd.read_csv('C:/Users/minji/PycharmProjects/COMP545Algorithm/Book12.csv')
df
#
# fields =[]
# rows=[]
#
# with open('Book1.xlsx','r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     fields = csvreader.next()
#     for row in csvreader:
#         rows.append(row)
#
#     print("Total no. of rows: %d"%(csvreader.line_num))
#
# print("Field names are: ' + ', ".join(field for field in fields))
#
# print("\nFirst 5 rows are;\n")
# for row in rows[:5]:
#     for col in row:
#         print("%10s"%col),
#     print("\n")




'''
with open('./Book2.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count=0
    for row in csv_reader:
        if line_count ==0:
            print(f'Colum names are {", ".join(row)}')
            line_count+=1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count+=1
    print(f'Processed {line_count} lines.')
'''

# us_holidays = holidays.UnitedStates()
# print(date(2018,11,23) in us_holidays)
# print(us_holidays.get('2018-11-23'))
# print(calendar.calendar(2018))


class Account:
    num_accounts = 0
    def __init__(self,name):
        self.name = name
        Account.num_accounts+=1
    def __del__(self):
        Account.num_accounts-=1

kim = Account("kim")
lee = Account("lee")
park = Account("park")
# print(Account.num_accounts)



'''
<Reference>

https://pypi.org/project/holidays/
'''