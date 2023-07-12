#!/usr/bin/env python

# A dummy API to receive request and return response of OK or False
#!/usr/bin/env python

import sys, json, os, random, string
import datetime as dt
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

@app.route("/accounts/submission/json", methods=["POST"])
def submissionJSON():
    input=request.json
    # Load data into dictionary so we can check fields
    requiredFields={"companyDetails": ["number","name"], 
                    "balanceSheetDate": ["year","month","day"],
                    "accounts": ["shareholdersFund","cash","netAssets"],
                    "statement": {"yearEnding": ["year", "month", "day"]},
                    "approval": [ "year", "month", "day"],
                    "presenter": ["contact","companyName","address"]}
    
    data=json.loads(input)
    print(data)

    twoChars=random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)
    subid=dt.datetime.now()
    result={"status": "ok", "submissionId": twoChars+subid.strftime("%Y%m%d%H%I%S")}

    topLevel=set(list(requiredFields.keys()))
    inTopLevel=set(list(data.keys()))
    if topLevel.difference(inTopLevel):
        result={"status": "FAILED"}

    # Check sub levels
    for sublevel in requiredFields:
        req=set(requiredFields[sublevel])
        inreq=set(data[sublevel])
        if req.difference(inreq):
            result={"status": "FAILED"}

    return(json.dumps(result))

@app.route("/accounts/submission/csv", methods=["POST"])
def submissionCSV():
    input=request.json

    twoChars=random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)
    subid=dt.datetime.now()
    result={"status": "ok", "submissionId": twoChars+subid.strftime("%Y%m%d%H%I%S")}

    # Data is a CSV so split into a list and make sure we have correct number of fields
    data=input.split(", ")
    data=input.split("\n")
    print(data)
    for lines in data:
        fields=lines.split(",")
        if len(fields) < 32:
            result={"status": "FAILED"}
            break

    return(json.dumps(result))

@app.route("/accounts/status")
def accountsStatus():
    state={"status": "ok"}
    return(json.dumps(state))

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0',port=8080,debug=True)
    except Exception as e:
        print(str(e))
        pass
 