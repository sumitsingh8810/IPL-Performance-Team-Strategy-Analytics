import pandas as pd

data2 = pd.read_csv('ipl_deliveries_2020_2025.csv')

data2.columns = data2.columns.str.strip().str.title()

text_columns = ['Batting_Team','Bowling_Team','Batter','Bowler','Dismissal_Type','Extra_Type']

for i in text_columns:
    data2[i] = data2[i].str.strip().str.title()

data2.to_csv('ipl_deliveries_2020_2025_cleaned_data.csv',index=False)
