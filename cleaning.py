import pathlib
import pandas as pd
import os

flist = []
dict_duplicates = {}
dict_names = {}
# reading each participant file
for file in pathlib.Path('new_data').iterdir():
    dataframe = pd.read_csv(file)
    # extracting the subject ids
    pid = str(dataframe['subject_id'].iloc[0])
    # extracting bonus payments
    bonus_amount = str(dataframe['stimulus'].iloc[-1].split('<p>')[3][22:])
    
    # cleaning data
    if pid == 'nan':
        os.remove(file) # remove file without subject id
    else: 
        # remove files with duplicate subject ids
        if pid in dict_duplicates:
            if dict_duplicates[pid] >= bonus_amount:
                os.remove(file)
            else:
                os.remove(dict_names[pid])
                dict_duplicates[pid] = bonus_amount
                dict_names[pid] = file
        else:
            dict_duplicates[pid] = bonus_amount
            dict_names[pid] = file

print(len(dict_duplicates))

