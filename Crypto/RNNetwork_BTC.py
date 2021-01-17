import pandas as pd
import os

SEQ_len = 60
PERIOD_PREDICT = 3
RATIO_TO_PREDICT = 'ETH_USD'

def Classify(current, future):
    if float(future)>float(current):
        return 1
    else:
        return 0

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
print(last_5)