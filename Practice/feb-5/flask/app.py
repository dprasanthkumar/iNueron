from flask import Flask,request,render_template

app = Flask(__name__)
#@ indicates route
#"/" indicates its my home page
@app.route("/")
def name():
    return render_template("index.html")

@app.route("/aboutme")
def aboutme():
    return("I am working in Mphasis")

@app.route('/operation',methods=['POST'])# in place os demo we replaces it with operarion
def math_operation():
    if (request.method=='POST'):
        operation=request.form['operation']# in place of json we are replacing it with form
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=0

        if operation=="add":
            result=num1+num2
        elif operation=="Mul":
            result=num1*num2
        elif operation=="div":
            result=num1/num2
        else:
            result=num1-num2

        return render_template("result.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
#############################################################################################
from flask import Flask,request,render_template

app = Flask(__name__)
#@ indicates route
#"/" indicates its my home page
@app.route("/")
def name():
    return render_template("index.html")

@app.route("/aboutme")
def aboutme():
    return("I am working in Mphasis")

@app.route('/operation',methods=['POST'])# in place os demo we replaces it with operarion
def math_operation():
    if (request.method=='POST'):
        operation=request.form['operation']# in place of json we are replacing it with form
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=0

        if operation=="add":
            result=num1+num2
        elif operation=="Mul":
            result=num1*num2
        elif operation=="div":
            result=num1/num2
        else:
            result=num1-num2

        return "the operation is {} and the result is {}".format(operation,result)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
####################################################################################################################
from flask import Flask,request,render_template

app = Flask(__name__)
#@ indicates route
#"/" indicates its my home page
@app.route("/")
def name():
    return render_template("index.html")

@app.route("/aboutme")
def aboutme():
    return("I am working in Mphasis")

@app.route('/operation',methods=['POST'])# in place os demo we replaces it with operarion
def math_operation():
    if (request.method=='POST'):
        operation=request.form['operation']# in place of json we are replacing it with form
        num1=request.form['num1']
        num2=request.form['num2']
        result=0

        if operation=="add":
            result=num1+num2
        elif operation=="Mul":
            result=num1*num2
        elif operation=="div":
            result=num1/num2
        else:
            result=num1-num2

        return "the operation is {} and the result is {}".format(operation,result)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
####################################################################################################################
from flask import Flask,request

app = Flask(__name__)
#@ indicates route
#"/" indicates its my home page
@app.route("/")
def name():
    return ("Prasanth Kumar")

@app.route("/aboutme")
def aboutme():
    return("I am working in Mphasis")

@app.route('/demo',methods=['POST'])
def math_operation():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=request.json['num1']
        num2=request.json['num2']
        result=0

        if operation=="add":
            result=num1+num2
        elif operation=="Mul":
            result=num1*num2
        elif operation=="div":
            result=num1/num2
        else:
            result=num1-num2

        return "the operation is {} and the result is {}".format(operation,result)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
####################################################################################################################
from flask import Flask,request

app = Flask(__name__)
#@ indicates route
#"/" indicates its my home page
@app.route("/")
def name():
    return ("Prasanth Kumar")

@app.route("/aboutme")
def aboutme():
    return("I am working in Mphasis")

@app.route('/demo',methods=['POST'])
def math_operation():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=request.json['num1']
        num2=request.json['num2']
        result=num1 + num2

        return "the operation is {} and the result is {}".format(operation,result)

@app.route('/Mul',methods=['POST'])
def Mul_operation():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=request.json['num1']
        num2=request.json['num2']
        result=num1 * num2

        return "the operation is {} and the result is {}".format(operation,result)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
####################################################################################################################
from flask import Flask,request

app = Flask(__name__)
#@ indicates route
#"/" indicates its my home page
@app.route("/")
def name():
    return ("Prasanth Kumar")

@app.route("/aboutme")
def aboutme():
    return("I am working in Mphasis")

@app.route('/demo',methods=['POST'])
def math_operation():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=request.json['num1']
        num2=request.json['num2']
        result=num1 + num2

        return "the operation is {} and the result is {}".format(operation,result)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
####################################################################################################################
from flask import Flask,request,render_template

app = Flask(__name__)
#@ indicates route
#"/" indicates its my home page
@app.route("/")
def name():
    return render_template("index.html")

@app.route("/aboutme")
def aboutme():
    return("I am working in Mphasis")

@app.route('/operation',methods=['POST'])# in place os demo we replaces it with operarion
def math_operation():
    if (request.method=='POST'):
        operation=request.form['operation']# in place of json we are replacing it with form
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=0

        if operation=="add":
            result=num1+num2
        elif operation=="Mul":
            result=num1*num2
        elif operation=="div":
            result=num1/num2
        else:
            result=num1-num2

        return render_template("result.html",result=result)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
