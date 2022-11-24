import flask
from flask import request, jsonify, current_app
from flask_cors import CORS
import pickle
import json
from pandas import json_normalize
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
from Config import *
from BaseController import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["ENV"] = "production"
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# filename = 'regrTSLA_model.sav'
# regr_model = pickle.load(open(filename, 'rb'))

@app.route('/home', methods=['GET'])
def home():
    return '''<h1>API IS RUNNING</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/api/predict', methods=['POST'])
def predictAlgo():
  print(request.headers.get('Content-Type'))
  args = request.json
  print(args)
  dto = '''{dataRequest}'''
  dto = dto.format(dataRequest = args)
  #dict = json.loads(str(dto))
  dataTest = json_normalize(args['request'])
  symbols = args['symbols']
  print(symbols)
  y_pred_api = ProcessPrediction(symbols, dataTest)
  return jsonify(
            Status = STATUS_SUCCESS_API,
            Data = y_pred_api,
            Message = CONTENT_INFOR_SUCCESS
            )

# @app.route('/api/training', methods=['POST'])
# def trainingAlgo():
#   print(request.headers.get('Content-Type'))
#   args = request.json
#   print(args)
#   dto = '''{dataRequest}'''
#   dto = dto.format(dataRequest = args)
#   #dict = json.loads(str(dto))
#   dateTime = args['date']
#   symbols = args['symbols']
#   y_pred_api = ProcessTraining(symbols, str(dateTime))
#   return jsonify(
#             Status = STATUS_SUCCESS_API,
#             Data = y_pred_api,
#             Message = CONTENT_INFOR_SUCCESS
#             )

@app.route('/api/gnb', methods=['POST'])
def predictAlgoGNB():
  args = request.json
  #print(args)
  dto = '''{dataRequest}'''
  #dto = dto.format(dataRequest = args)
  #dict = json.loads(str(dto))
  df_r = pd.DataFrame(args)
  df_r['Score'] = df_r['Score1'] + df_r['Score2'] + df_r['Score3'] + df_r['Score4'] + df_r['Score5'] + df_r['Score6'] + df_r['Score8'] + df_r['Score9'] + df_r['Score10']
  y_pred_api = ProcessPredictionGNB('', df_r)
  print(y_pred_api)
  return jsonify(
            Status = STATUS_SUCCESS_API,
            Data = str(y_pred_api),
            Message = CONTENT_INFOR_SUCCESS
          )

@app.route('/api/rfc', methods=['POST'])
def predictAlgoRFC():
  args = request.json
  #print(args)
  dto = '''{dataRequest}'''
  #dto = dto.format(dataRequest = args)
  #dict = json.loads(str(dto))
  df_r = pd.DataFrame(args)
  df_r['Score'] = df_r['Score1'] + df_r['Score2'] + df_r['Score3'] + df_r['Score4'] + df_r['Score5'] + df_r['Score6'] + df_r['Score8'] + df_r['Score9'] + df_r['Score10']
  y_pred_api = ProcessPredictionRFC('', df_r)
  print(y_pred_api)
  return jsonify(
            Status = STATUS_SUCCESS_API,
            Data = str(y_pred_api),
            Message = CONTENT_INFOR_SUCCESS
          )
if __name__ == "__main__":
    app.run(host=HOST, port=PORT)