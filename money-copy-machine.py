import time
import pyupbit
import datetime

access = "3fCmuKAoYgzFhxbSApVwCYpGhoH6Ml9zaCcxd8SH"
secret = "WmMPxyz91TNO71m1j4sEK18gpO3SvhIxdCxU6nCP"

a = 0.5
interval_time = "minute15"
stockName = "KRW-BTC"
coinName = "BTC"
fee = 0.04

def get_target_price(ticker, k) :
    df = pyupbit.get_ohlcv(ticker, interval = interval_time, count = 2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker) :
    df = pyupbit.get_ohlcv(ticker, interval = interval_time, count = 1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker) :
    balances = upbit.get_balances()
    for b in balances :
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker) :
    return pyupbit.get_orderbook(ticker = ticker)["orderbook_units"][0]["ask_price"]


upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time(stockName)
        end_time = start_time + datetime.timedelta(minutes = 15)

        if start_time < now < end_time - datetime.timedelta(seconds=60):
            target_price = get_target_price(stockName, a)
            current_price = get_current_price(stockName)
            if target_price <= current_price:
                krw = get_balance("KRW")
                if krw > 5000 :
                    upbit.buy_market_order(stockName, krw * (1 - fee))
        else:
            btc = get_balance(coinName)
            if btc > 0.00008 :
                upbit.sell_market_order(stockName, btc)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)