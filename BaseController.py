import pyodbc
from Config import *
import os
import pickle
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from joblib import dump, load

#conn = pyodbc.connect(CONNECTION_STRING)

# def GetSymbols():
#     cursor = conn.cursor()
#     cursor.execute('select DISTINCT Symbol from AlgoBackTestTradeSetupOrderHistory')
#     while 1:
#         row = cursor.fetchall()
#         if not row:
#             break
#         print(row.Symbol)
#     return

# def ProcessTraining(symbol,dateTime):
#     # cursor = conn.cursor()
#     # cursor.execute('EXEC UOMLQuery ' + "'"+Symbol+"'" + "'"+dateTime+"'")
#     # records = cursor.fetchall()
#     rows = pd.read_sql_query('EXEC UOMLQuerySymbol ' + "'"+dateTime+"'," + "'"+symbol+"'", conn)
#     df = pd.DataFrame(rows, columns=COLUMNS)
#     #df.to_csv('example2.csv', index=False)

#     filename = 'regr'+symbol+'_model.sav'
#     pathModel = os.path.join(OS_PWD, 'Models', filename)
#     if (CheckModelsExists(pathModel)):
#         statusModel = True
#         regr_model = pickle.load(open(pathModel, 'rb'))
#         Training(symbol, df, model=regr_model, statusModel=statusModel)
#     else:
#         statusModel = False
#         Training(symbol, df, model=None, statusModel=statusModel)
#         return
    
#     return

def ProcessPredictionGNB(nameSymbol, dataRequest):
    try:
        check = Check(dataRequest)
        if(check):
            clf = load('model/models/gnb1.joblib')
            y_pred = clf.predict(dataRequest)
            return y_pred[0]
        else:
            return CONTENT_INFOR_FAIL_PREDICT
    except Exception as e:
        print("Catch:")
        print(e)
        return e.args

def ProcessPredictionGNB(nameSymbol, dataRequest):
    try:
        check = Check(dataRequest)
        if(check):
            clf = load('model/models/gnb1.joblib')
            y_pred = clf.predict(dataRequest)
            return y_pred[0]
        else:
            return CONTENT_INFOR_FAIL_PREDICT
    except Exception as e:
        print("Catch:")
        print(e)
        return e.args

def ProcessPredictionRFC(nameSymbol, dataRequest):
    try:
        check = Check(dataRequest)
        if(check):
            clf = load('model/models/rfc1.joblib')
            y_pred = clf.predict(dataRequest)
            return y_pred[0]
        else:
            return CONTENT_INFOR_FAIL_PREDICT
    except Exception as e:
        print("Catch:")
        print(e)
        return e.args

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

def Check(df_arr):
    df_arr = df_arr.values.tolist()
    df_arr = df_arr[0]
    print(df_arr)
    col_names = ['Symbol', 'PutCall', 'StrikePrice', 'Date', 'ExpirationNum', 'Expiration', 'Score1', 'Score2', 'Score3', 'Score4', 'Score5', 'Score6', 'Score8', 'Score9', 'Score10', 'Score', 'P', 'P1', 'P2']
    print(len(col_names))
    # load dataset
    pima = pd.read_csv("newv5.csv", header=None, names=col_names)
    pima = pima.drop_duplicates()
    pima = pima.iloc[1:]
    pima["ExpirationInt"] = pd.to_datetime(pima['Expiration'])


    pima['PutCall'] = pima['PutCall'].astype(float)
    pima['StrikePrice'] = pima['StrikePrice'].astype(float)
    pima["Day"] = pima['ExpirationInt'].dt.day
    pima["Month"] = pima['ExpirationInt'].dt.month
    pima["Year"] = pima['ExpirationInt'].dt.year
    pima['Score1'] = pima['Score1'].astype(float)
    pima['Score2'] = pima['Score2'].astype(float)
    pima['Score3'] = pima['Score3'].astype(float)
    pima['Score4'] = pima['Score4'].astype(float)
    pima['Score5'] = pima['Score5'].astype(float)
    pima['Score6'] = pima['Score6'].astype(float)
    pima['Score8'] = pima['Score8'].astype(float)
    pima['Score9'] = pima['Score9'].astype(float)
    pima['Score10'] = pima['Score10'].astype(float)
    pima['Score'] = pima['Score'].astype(float)
    #input chuyen thanh array theo thu tu
    #df_arr = [2.0, 292.5, 16, 9, 2022, 0.0, 1.25, 3.75, 4.46, 0.0, 0.01, 1.5, 0.0, 5.0, 15.97]
    check = pima.loc[(pima['PutCall']==df_arr[0]) & 
                    (pima['StrikePrice']== df_arr[1]) & 
                    (pima['Day']== df_arr[2])& 
                    (pima['Month']== df_arr[3])& 
                    (pima['Year']== df_arr[4]) & 
                    (pima['Score1']== df_arr[5])& 
                    (pima['Score2']== df_arr[6])& 
                    (pima['Score3']== df_arr[7])& 
                    (pima['Score4']== df_arr[8])& 
                    (pima['Score5']== df_arr[9])& 
                    (pima['Score6']== df_arr[10])& 
                    (pima['Score8']== df_arr[11])& 
                    (pima['Score9']== df_arr[12])& 
                    (pima['Score10']== df_arr[13])& 
                    (pima['Score']== df_arr[14]),
                        ['P']]
    if(len(check) > 0):
        return True
    else:
        return False

# ProcessTraining('TSLA','2022-09-16')