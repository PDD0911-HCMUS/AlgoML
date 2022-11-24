
import pandas as pd
col_names = ['Symbol', 'PutCall', 'StrikePrice', 'Date', 'ExpirationNum', 'Expiration', 'Score1', 'Score2', 'Score3', 'Score4', 'Score5', 'Score6', 'Score8', 'Score9', 'Score10', 'Score', 'P', 'P1', 'P2']
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
df_arr = [2.0, 292.5, 16, 9, 2022, 0.0, 1.25, 3.75, 4.46, 0.0, 0.01, 1.5, 0.0, 5.0, 15.97]
check = pima.loc[(pima['PutCall']==df_arr[0]) & (pima['StrikePrice']== df_arr[1]) & (pima['Day']== df_arr[2])& (pima['Month']== df_arr[3])& (pima['Year']== df_arr[4]) & (pima['Score1']== df_arr[5])& (pima['Score2']== df_arr[6])& (pima['Score3']== df_arr[7])& (pima['Score4']== df_arr[8])& (pima['Score5']== df_arr[9])& (pima['Score6']== df_arr[10])& (pima['Score8']== df_arr[11])& (pima['Score9']== df_arr[12])& (pima['Score10']== df_arr[13])& (pima['Score']== df_arr[14]),
                    ['P']]

print(len(check))

#Neu check size > 0 thi predict models
