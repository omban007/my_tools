import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

sns.set()

df = pd.read_csv(r'C:\Users\Demon\PycharmProjects\DS\data\ADANIPOWER_NS.csv')
df.head()


def pct_change(x, period=1):
    x = np.array(x)
    return (x[period:] - x[:-period]) / x[:-period]


number_simulation = 100
predict_day = 30

results = pd.DataFrame()

for i in tqdm(range(number_simulation)):
    prices = df.Close.values[-predict_day:].tolist()
    volatility = pct_change(prices[-predict_day:]).std()
    for d in range(predict_day):
        prices.append(prices[-1] * (1 + np.random.normal(0, volatility)))
        volatility = pct_change(prices[-predict_day:]).std()
    results[i] = pd.Series(prices[-predict_day:]).values

plt.figure(figsize=(10, 5))
plt.plot(results)
plt.ylabel('Value')
plt.xlabel('Simulated days')
plt.show()

raveled = results.values.ravel()
raveled.sort()
cp_raveled = raveled.copy()

plt.figure(figsize=(17, 5))
plt.subplot(1, 3, 1)
plt.plot(results)
plt.ylabel('Value')
plt.xlabel('Simulated days')
plt.subplot(1, 3, 2)
sns.distplot(df.Close, norm_hist=True)
plt.title('$\mu$ = %.2f, $\sigma$ = %.2f' % (df.Close.mean(), df.Close.std()))
plt.subplot(1, 3, 3)
sns.distplot(raveled, norm_hist=True, label='monte carlo samples')
sns.distplot(df.Close, norm_hist=True, label='real samples')
plt.title('simulation $\mu$ = %.2f, $\sigma$ = %.2f' % (raveled.mean(), raveled.std()))
plt.legend()
plt.show()
