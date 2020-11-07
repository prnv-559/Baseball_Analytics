from pybaseball import pitching_stats, batting_stats
from collections import Counter
import pandas as pd
import os
import csv

#batters
batter_data = batting_stats(2018, 2019, qual=502)
batter_data.head(0).to_csv("batters.csv", index = False, sep=',', encoding='utf-8')

counter = {}
for b in batter_data.IDfg:
    counter[b] = counter.get(b, 0) + 1
idfg = ([key for key, count in counter.items() if count == 2])
print(idfg)

batter_data.set_index("IDfg", inplace=True)
batter_data.head(1000)
for batters in idfg:
    print(batter_data.loc[batters])
    with open("batters.csv", 'a') as f:
        batter_data.loc[batters].to_csv(f, header=False)

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