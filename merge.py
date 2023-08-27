import pathlib
import pandas as pd
import csv

df = pd.DataFrame()
# reading each participant file
for file in pathlib.Path('new_data').iterdir():
    dataframe = pd.read_csv(file)
    dataframe = dataframe.loc[dataframe['outcome'].notnull()]
    dataframe.drop([ # unwanted columns
        'stimulus', 
        'trial_type', 
        'trial_index', 
        'time_elapsed', 
        'internal_node_id', 
        'accuracy'
    ], axis = 1, inplace = True)
    dataframe['block'] = dataframe['block'] + 1
    
    block = dataframe.loc[dataframe['block'] == 1.0]
    s = sum(block['outcome'])
    # mentioning the choice domain and order of the domain
    if s > 0:
        domain = ['Gain' for x in range(100)]
        domain.extend(['Loss' for x in range(100)])
        order = ['Gain & Loss' for x in range(200)]
    else:
        domain = ['Loss' for x in range(100)]
        domain.extend(['Gain' for x in range(100)])
        order = ['Loss & Gain' for x in range(200)]            

    dataframe['domain'] = domain
    dataframe['order'] = order
    
    # merging data
    df = pd.concat([df, dataframe], ignore_index = True)

# converting into csv
df.to_csv('choice_game.csv', index = False)