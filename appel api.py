from flask import Flask, jsonify
import pandas as pd
import sqlalchemy as sqla


URI  = "mysql://root:master2@localhost/data"
con = sqla.create_engine(URI)


app =  Flask(__name__)




@app.route('/raw/<ticker>', methods=['GET'])
def raw_ticker(ticker):
    req = pd.read_sql("SELECT {}, Date FROM raw_true".format(str(ticker)), con = con)
    data = { "data": req.to_dict(orient = "records")} #df.to_dict(orient = "records")
    return jsonify(data)


@app.route('/raw', methods=['GET'])
def raw():
    req = pd.read_sql("SELECT * FROM raw_true", con = con)
    data = { "data": req.to_dict(orient = "records")} #df.to_dict(orient = "records")
    return jsonify(data)



@app.route('/modified', methods=['GET'])
def modified():
    req = pd.read_sql("SELECT *FROM modified", con = con)
    data = { "data": req.to_dict(orient = "records")} #df.to_dict(orient = "records")
    return jsonify(data)


@app.route('/modified/<ticker>', methods=['GET'])
def modified_ticker(ticker):
    req = pd.read_sql("SELECT {}, stats FROM modified".format(str(ticker)), con = con)
    data = { "data": req.to_dict(orient = "records")} #df.to_dict(orient = "records")
    return jsonify(data)

#@app.route('/raw/<symbol>', methods=['GET'])
#def helloworld(symbol):
#    req = pd.read_sql("SELECT * FROM raw", con = con)
#    data = { "symbol" : str(symbol) ,"data": req[str(symbol)].to_dict(orient = "records")} #df.to_dict(orient = "records")
#    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port = 9000)