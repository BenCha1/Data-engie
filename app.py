from flask import Flask, jsonify
import pandas as pd


app =  Flask(__name__)


@app.route('/raw/<ticker>', methods=['GET'])
def raw_ticker(ticker):
    req = pd.read_csv("raw_final_true")
    data = { "data": req[[str(ticker), "Date"]].to_dict(orient = "records")} #df.to_dict(orient = "records")
    return jsonify(data)


@app.route('/raw', methods=['GET'])
def raw():
    req = pd.read_csv("raw_final_true")
    data = { "data": req.to_dict(orient = "records")} #df.to_dict(orient = "records")
    return jsonify(data)



@app.route('/modified', methods=['GET'])
def modified():
    req = pd.read_csv("modified_true.csv")
    data = { "data": req.to_dict(orient = "records")} #df.to_dict(orient = "records")
    return jsonify(data)


@app.route('/modified/<ticker>', methods=['GET'])
def modified_ticker(ticker):
    req = pd.read_csv("modifier_true.csv")
    data = { "data": req[[str(ticker), "stats"]].to_dict(orient = "records")} #df.to_dict(orient = "records")
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)