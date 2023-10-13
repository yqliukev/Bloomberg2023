import pandas as pd
import os
import yfinance as yf

from util.portList import getStocks
from util.calculations import (calcMA,
                               calcLower,
                               calcBoll)

cwd = os.getcwd()

def loadTicker(stockList):
    stockString = ""
    for stock in stockList:
        stockString = stockString + " " + stock
    portData = yf.download(stockString, period = "2y", group_by = "ticker")
    return portData


def main():
    stockList = getStocks()
    portData = calcBoll(loadTicker(stockList), stockList)
    portData = portData.iloc[::-1]
    portData.to_csv(os.path.join(cwd, "PortData.csv"))

main()