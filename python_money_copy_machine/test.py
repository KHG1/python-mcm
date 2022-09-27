import pyupbit
import numpy as np

k = 0.5

df = pyupbit.get_ohlcv("KRW-BTC", interval="minute10", count = 10)
df['range'] = (df['high'] - df['low']) * k
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.05

df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")