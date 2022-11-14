import pyodbc
from Config import *
import os
import pickle
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

conn = pyodbc.connect(CONNECTION_STRING)

def GetSymbols():
    cursor = conn.cursor()
    cursor.execute('select DISTINCT Symbol from AlgoBackTestTradeSetupOrderHistory')
    while 1:
        row = cursor.fetchall()
        if not row:
            break
        print(row.Symbol)
    return

def ProcessTraining(symbol,dateTime):
    # cursor = conn.cursor()
    # cursor.execute('EXEC UOMLQuery ' + "'"+Symbol+"'" + "'"+dateTime+"'")
    # records = cursor.fetchall()
    rows = pd.read_sql_query('EXEC UOMLQuerySymbol ' + "'"+dateTime+"'," + "'"+symbol+"'", conn)
    df = pd.DataFrame(rows, columns=COLUMNS)
    #df.to_csv('example2.csv', index=False)

    filename = 'regr'+symbol+'_model.sav'
    pathModel = os.path.join(OS_PWD, 'Models', filename)
    if (CheckModelsExists(pathModel)):
        statusModel = True
        regr_model = pickle.load(open(pathModel, 'rb'))
        Training(symbol, df, model=regr_model, statusModel=statusModel)
    else:
        statusModel = False
        Training(symbol, df, model=None, statusModel=statusModel)
        return
    
    return

def ProcessPrediction(nameSymbol, dataRequest):
    try:
        filename = 'regr'+nameSymbol+'_model.sav'
        pathModel = os.path.join(OS_PWD, 'Models', filename)
        if (CheckModelsExists(pathModel)):
            regr_model = pickle.load(open(pathModel, 'rb'))
            y_pred_api = regr_model.predict(dataRequest)
            return y_pred_api[0]
        else:
            return CONTENT_INFOR_FAIL_LOAD_MODEL
    except Exception as e:
        print("Catch:")
        print(e)
        return e.args

def CheckModelsExists(pathModel):
    isExists = False
    if(os.path.exists(pathModel)):
        isExists = True
    return isExists

def Training(symbols, dataFrame, model = None, statusModel = False):
    X = dataFrame[['PutCall', 'StrikePrice', 'ExpirationNum', 'Score1', 'Score2', 'Score3', 'Score4', 'Score5', 'Score6', 'Score8', 'Score9', 'Score10', 'TotalScore']]
    y = dataFrame['P']
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=42)
    if(statusModel == True):
        model.fit(X_train, y_train)
        filename = 'regr'+symbols+'_model.sav'
        pathModel = os.path.join(OS_PWD, 'Models', filename)
        pickle.dump(model, open(pathModel, 'wb'))
    elif(statusModel == False):
        model = linear_model.LinearRegression()
        model.fit(X_train, y_train)
        filename = 'regr'+symbols+'_model.sav'
        pathModel = os.path.join(OS_PWD, 'Models', filename)
        pickle.dump(model, open(pathModel, 'wb'))



# ProcessTraining('TSLA','2022-09-16')