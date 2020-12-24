import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR

df_btc = pd.read_csv('C:\\Users\\viet tran\\Desktop\\Python\\Crypto\\BTC_USD.csv')
df_eth = pd.read_csv('C:\\Users\\viet tran\\Desktop\\Python\\Crypto\\ETH_USD.csv')

#remove unnecessary columns
df_btc.drop(['Currency', 'Date', '24h Open (USD)', '24h High (USD)', '24h Low (USD)'],1,inplace = True)

# shift n prediction days up
prediction_days = 30
df_btc['Prediction'] = df_btc['Closing Price (USD)'].shift(-prediction_days)


# independent dataset X in array without n prediction days
X = np.array(df_btc.drop(['Closing Price (USD)'],1))
X = X[:len(df_btc)-prediction_days]

# dependent dataset Y in array without n prediction days
y = np.array(df_btc['Closing Price (USD)'])
y = y[:len(df_btc)-prediction_days]

#20% test 80% training
x_train, x_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)

#prediction_days_array = np.array(df.drop(['Prediction_BTC'],1))[-prediction_days:]


#support vector machine (Regression)
svr = SVR(kernel='rbf', C=1e3, gamma = 0.00001)
svr.fit(x_train, y_train)
svr_confidence = svr.score(x_test, y_test)
print("svr accuracy: ", svr_confidence)

svr_prediction = svr.predict(x_test)

plt.scatter(svr_prediction, y_test)
plt.show()

'''
for i,j in zip(df.columns.values, range(2)): 
	temp = 211 + j
	plt.subplot(temp)
	plt.plot(df[i], label = i)	
	plt.legend(loc = 'upper left')
	plt.xlabel('Time')
	plt.ylabel('Price ($)')

plt.show()
'''