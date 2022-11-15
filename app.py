from flask import Flask, jsonify
import pandas as pd


app =  Flask(__name__)

@app.route('/hello', methods=['GET'])
def helloworld():
    req = pd.read_csv("raw_final.csv")
    data = { "data": req.to_dict(orient = "records")} #df.to_dict(orient = "records")
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)