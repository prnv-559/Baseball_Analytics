from pybaseball import pitching_stats, batting_stats
from collections import Counter
import pandas as pd
import os
import csv

#batters
batter_data = batting_stats(2015, 2019, qual = 100)
batter_data.head(0).to_csv("batters.csv", index = False, sep=',', encoding='utf-8')

df = pd.DataFrame(batter_data)
df.sort_values(by=["Season"], inplace=True)
print(df)


counter = {}
for b in df.IDfg:
    counter[b] = counter.get(b, 0) + 1
idfg = ([key for key, count in counter.items() if count == 5])
print(idfg)

df.set_index("IDfg", inplace=True)
df.head(1000)
for id in idfg:
    print(df.loc[id])
    #batter_data.set_index("Season", inplace=True)
    with open("batters.csv", 'a+') as f:
        df.loc[id].to_csv(f, header=False)


'''
#pitchers
pitcher_data = pitching_stats(2018, 2019, qual=162)
pitcher_data.head(0).to_csv("pitchers.csv", index = False, sep=',', encoding='utf-8')

counter = {}
for p in pitcher_data.IDfg:
    counter[p] = counter.get(p, 0) + 1
idfg = ([key for key, count in counter.items() if count == 2])
print(idfg)

pitcher_data.set_index("IDfg", inplace=True)
pitcher_data.head(1000)
for pitchers in idfg:
    print(pitcher_data.loc[pitchers])
    with open("pitchers.csv", 'a') as f:
        pitcher_data.loc[pitchers].to_csv(f, header=False)
'''