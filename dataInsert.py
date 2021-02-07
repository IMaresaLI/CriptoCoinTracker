from databaseConnect import *
import requests
import datetime



def getData(coinData):
    data = getDatabase(coinData)
    return data


def InsertData():
    list = ["USD","TRY","EUR"]
    time = datetime.datetime.now()
    for i in list:
        a = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency={i}&order=market_cap_desc&per_page=100&page=1&sparkline=false")
        response_json = a.json()
        for j in response_json:
            if j["id"] == "bitcoin":
                if str(j["current_price"]) == getData("Bitcoin"+i)[-1][1]:
                    pass                
                else :
                    Add(f"Bitcoin{i}",j["name"],j["current_price"],j["low_24h"],j["high_24h"],time)
            if j["id"] == "dogecoin":
                if str(j["current_price"]) == getData("Doge"+i)[-1][1]:
                    pass                
                else :
                    Add(f"Doge{i}",j["name"],j["current_price"],j["low_24h"], j["high_24h"],time)
            if j["id"] == "ripple":
                if str(j["current_price"]) == getData("Ripple"+i)[-1][1]:
                    pass                
                else :
                    Add(f"Ripple{i}",j["name"],j["current_price"],j["low_24h"], j["high_24h"],time)


