import os

MY_DB = ['BacktestResultDB', 'TMP']

CONNECTION_STRING = (
    r'Driver=SQL Server;'
    r'Server=DESKTOP-RS22QF8;'
    r'Database=BacktestResultDB;'
    r'Trusted_Connection=yes;'
    )

HOST = '10.70.38.171'
PORT = 8009

STATUS_SUCCESS_API = 1
STATUS_FAIL_API = 2
STATUS_FAIL_READFILE = 3
CONTENT_INFOR_SUCCESS = 'Predict Done !!!'
CONTENT_INFOR_FAIL_LOAD_MODEL = 'Model is not existed !!!'
CONTENT_INFOR_FAIL_PREDICT = 'The data request is not existed in Database !!!'
OS_PWD = os.getcwd()

COLUMNS = ['OptionTradeId', 'TradeGuid', 'RuleClassId', 'TradePLPerc', 'TradePL', 'RowNumber', 'Id', 'Symbol', 'PutCall', 'Description', 
            'StrikePrice', 'Date', 'Time', 'DateTime', 'Expiration', 'Ask', 'Bid', 'BasicCost', 'Midpoint', 'OpenInterest', 'Price', 'Size', 'TradeCount', 'UnderlyingPrice', 'UnderlyingType',
            'Volume', 'OptionActivityType', 'OptionActivityType', 'OptionalSymbol', 'Sentiment', 'UpdateTime', 'Score1', 'Score2', 'Score3', 'Score4', 'Score5', 'Score6', 'Score7', 'Score8',
            'Score9', 'Score10', 'Score11', 'Score12', 'Score13', 'Score14', 'Score15', 'TotalScore', 'Aggressorlnd', 'JsonData', 'P', 'DTE']