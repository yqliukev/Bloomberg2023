
def calcBoll(portData, stockList):
    for stock in stockList:
        portData[stock] = portData[stock].dropna()
        portData.loc[:, (stock, 'SMA20')] = portData[stock]['Close'].dropna().rolling(20).mean()
        portData.loc[:, (stock, 'SD20')] = portData[stock]['Close'].dropna().rolling(20).std()
        portData.loc[:, (stock, 'BollHIGH')] = portData[stock]['SMA20'] + portData[stock]['SD20'] * 2
        portData.loc[:, (stock, 'BollLOW')] = portData[stock]['SMA20'] - portData[stock]['SD20'] * 2
    return portData

## take in stock table
def calcMA(stockData, days, exponential = False):
    if not exponential:
        return stockData[:days].mean()

def calcLower(stockData, days, exponential = False):
    if not exponential:
        return stockData[:days].std()
