import time
import pyupbit
import datetime

access = "3fCmuKAoYgzFhxbSApVwCYpGhoH6Ml9zaCcxd8SH"
secret = "WmMPxyz91TNO71m1j4sEK18gpO3SvhIxdCxU6nCP"

k = 0.5
ticker = "KRW-BTC"
coinName = "BTC"
fee = 0.05

def get_target_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="minute10", count=1)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute10", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]


upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time(ticker)
        end_time = start_time + datetime.timedelta(minutes = 10)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price(ticker, k)
            current_price = get_current_price(ticker)
            if target_price < current_price:
                krw = get_balance(ticker)
                if krw > 5000:
                    upbit.buy_market_order(ticker, krw*(1-fee))
        else:
            btc = get_balance(coinName)
            if btc > 0.00008:
                upbit.sell_market_order(ticker, btc*(1-fee))
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)