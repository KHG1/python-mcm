from turtle import up
import pyupbit

access = "3fCmuKAoYgzFhxbSApVwCYpGhoH6Ml9zaCcxd8SH"
secret = "WmMPxyz91TNO71m1j4sEK18gpO3SvhIxdCxU6nCP"

a = 0.3
stockName = "KRW-BTC"
coinName = "BTC"
fee = 0.05

upbit = pyupbit.Upbit(access, secret)

balances = upbit.get_balances()

if balances == None :
    print("None")

else :
    print(balances[0]['currency'])