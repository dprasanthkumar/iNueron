from  flask import Flask,request

app=Flask(__name__)

@app.route("/")

def homepage():
    return "<h1>My name is Prasanth Kumar<h1>"

@app.route("/add",methods=['POST'])
def add():
    if request.method=="POST":
        result=int(request.json['num1'])+int(request.json['num2'])
        return "the sum is {}".format(result)

if  __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)\
    
####################################################################################################
from  flask import Flask,request

app=Flask(__name__)

@app.route("/")

def homepage():
    return "<h1>My name is Prasanth Kumar<h1>"

@app.route("/add",methods=['POST'])
def add():
    if request.method=="POST":
        result=request.json['num1']+request.json['num2']
        return "the sum is {}".format(result)

if  __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
    
####################################################################################################
from  flask import Flask,request,jsonify

app=Flask(__name__)

@app.route("/")

def homepage():
    return "<h1>My name is Prasanth Kumar<h1>"

@app.route("/add",methods=['POST'])
def add():
    if request.method=="POST":
        result=int(request.json['num1'])+int(request.json['num2'])
        return jsonify("the sum is {}".format(result))#b this will give us the format in json format

if  __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
