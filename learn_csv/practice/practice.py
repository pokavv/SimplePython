PATH = './learn_csv/practice/practice_data.csv'

# readlines()
'''
with open(PATH) as file:
    data = file.readlines()
    print(data)
'''

# csv lib
'''
import csv

with open(PATH) as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)
'''

# pandas lib
import pandas as pd

data = pd.read_csv(PATH)
'''
print(data)
print(type(data)) # DataFrame
print()
print(data['temp'])
print(type(data)) # Serise
'''

'''
# to_dict(pandas)
dict_data = data.to_dict()
print(dict_data)

# to_list(pandas)
temp_list = data['temp'].to_list()
print(temp_list)

# mean(pandas)
print(data['temp'].mean())

# max & min(pandas)
print(data['temp'].max())
print(data['temp'].min())

# get data in columns
print(data['condition'])
print(data.condition)

# get data in row
print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9 / 5 + 32
print(monday_temp_F)
'''

# create dataframe from scratch
data_dict = {
    'students': ['amy', 'james', 'angela'],
    'score': [75, 66, 94]
}
new_data = pd.DataFrame(data_dict)
print(new_data)
new_data.to_csv('./learn_csv/practice/new_practice_data.csv')