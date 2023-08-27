import pathlib
import pandas as pd
import csv
import json

attention = []
demo = []
# reading each file and extracting the questionnaires
for file in pathlib.Path('new_data').iterdir():
    dataframe = pd.read_csv(file)
    pid = str(dataframe['subject_id'].iloc[0])
    ques_demo = str(dataframe['response'].iloc[-2])
    ques_attention = str(dataframe['response'].iloc[-3])
    dict_demo = json.loads(ques_demo)
    del dict_demo['P0_Q0']
    dict_demo['subject_id'] = pid
    dict_attention = json.loads(ques_attention)
    del dict_attention['P0_Q0']
    dict_attention['subject_id'] = pid
    attention.append(dict_attention)
    demo.append(dict_demo)

# creating new csv files with the questionnaires    
with open('attention.csv', 'w', newline = '') as f:
    w = csv.DictWriter(f, attention[0].keys())
    w.writeheader()
    w.writerows(attention)

with open('demographics.csv', 'w', newline = '') as f:
    w = csv.DictWriter(f, demo[0].keys())
    w.writeheader()
    w.writerows(demo)


