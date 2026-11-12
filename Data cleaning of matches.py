import pandas as pd

data = pd.read_csv('ipl_matches_2020_2025.csv')


data['Date'] = pd.to_datetime(data['Date'])

str_data_columns = ['Team1','Team2','Venue','Toss_Winner','Toss_Decision','First_Innings_Team','Chasing_Team','Winner','Result_Type','Player_of_the_Match']


for i in str_data_columns:
    data[i] = data[i].str.strip()

for j in str_data_columns:
    data[j] = data[j].str.strip().str.title()


data.columns = data.columns.str.strip()

data.columns = data.columns.str.title()

data.to_csv('ipl_matches_cleaned_data.csv',index=False)

