import pandas as pd
import os
from sklearn import preprocessing
from collections import deque
import random
import numpy as np 

SEQ_len = 60
PERIOD_PREDICT = 3
RATIO_TO_PREDICT = 'ETH_USD'

def Classify(current, future):
    if float(future)>float(current):
        return 1
    else:
        return 0

#normalization 
def preprocess_df(df):
    df = df.drop('future',1)
    for col in df.columns:
        if col != 'target':
            df[col] = df[col].pct_change()
            df.dropna(inplace=True)
            df[col] = preprocessing.scale(df[col].values)
    df.dropna(inplace=True)
    sequential_data = []
    prev_days = deque(maxlen= SEQ_len)
    print(df.head())
    for c in df.columns:
        print(c)
    for i in df.values:
        prev_days.append([n for n in i[:-1]])
        if len(prev_days) == SEQ_len:
            sequential_data.append([np.array(prev_days), i[-1]]) 
    random.shuffle(sequential_data)


main_df = pd.DataFrame()
ratios = ['BTC_USD', 'ETH_USD']
for ratio in ratios:
    dataset = f"C:\\Users\\viet tran\\Desktop\\Python\\Crypto\\{ratio}.csv"
    df = pd.read_csv(dataset)
    #print(df.head())
    df.rename(columns={'Closing Price (USD)':f"{ratio}_Close"}, inplace=True)
    df = df[[f"{ratio}_Close"]]
    if len(main_df) == 0:
        main_df = df
    else:
        main_df = main_df.join(df)

main_df['future'] = main_df[f"{RATIO_TO_PREDICT}_Close"].shift(-PERIOD_PREDICT)
main_df['target'] = list(map(Classify, main_df[f"{RATIO_TO_PREDICT}_Close"], main_df['future']))

#print(main_df[[f"{RATIO_TO_PREDICT}_Close", "future", "target"]].head(20))

times = sorted(main_df.index.values)
last_5 = times[-int(0.05*len(times))]


validation_main_df = main_df[(main_df.index >= last_5)]
main_df = main_df[(main_df.index < last_5)]

preprocess_df(main_df)
#train_x, train_y = preprocess_df(main_df)
#valid_x, valid_y = preprocess_df(valid_main_df)