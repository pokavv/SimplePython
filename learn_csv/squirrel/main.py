import pandas as pd

PATH = './learn_csv/squirrel/2018_squirrel_data_in_central_park.csv'

data = pd.read_csv(PATH)

# gray squirrels
gray_squirrels = data[data['Primary Fur Color'] == 'Gray']
print(gray_squirrels)
print(len(gray_squirrels)) # 2473

# red squirrels
red_squirrels = data[data['Primary Fur Color'] == 'Cinnamon']
print(red_squirrels)
print(len(red_squirrels)) # 392

# black squirrels
black_squirrels = data[data['Primary Fur Color'] == 'Black']
print(black_squirrels)
print(len(black_squirrels)) # 103

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [len(gray_squirrels), len(red_squirrels), len(black_squirrels)]
}

new_df = pd.DataFrame(data_dict)
new_df.to_csv('./learn_csv/squirrel/squirrel_count_to_furcolor.csv')