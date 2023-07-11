#!/usr/bin/env python

# A dummy API to receive request and return response of OK or False
#!/usr/bin/env python

import sys, json, os
from flask import Flask, request
from flask_cors import CORS

global globalCount
globalCount=0

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    # General page
    return("<h1>Hello</h1>")

@app.route("/api/add/<num1>/<num2>", methods=["GET"])
def addNumbers(num1,num2):
    result={"result": num1+num2}
    return(json.dumps(result))

@app.route("/api/chkjson", methods=["POST"])
def checkJSON():
    result="FAILED"
    msg=""
    try:
        # If this works then OK
        input=request.json
        result="OK"
    except Exception as e:
        msg=str(e)
        pass

    finalresult={"result": result, "message": msg}
    return(json.dumps(finalresult))

@app.route("/api/chkcsv", methods=["POST"])
def checkCSV():
    result="OK"
    # If this works then OK
    input=request.json
    data=json.loads(input)

    if "," not in data["csv"]:
         result="FAILED"

    finalresult={"result": result}
    return(json.dumps(finalresult))

@app.route("/api/global", methods=["PUT"])
def updateGlobalCount():
    global globalCount
    input=request.json
    data=json.loads(input)
    num=data['num']
    globalCount=globalCount+num
    result={"result": globalCount}
    return(json.dumps(result))

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0',port=8080,debug=True)
    except Exception as e:
        print(str(e))
        pass
 