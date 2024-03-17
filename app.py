from doctest import debug
import json
from flask import Flask, render_template, request,redirect,send_file, session
# import pandas as pd
from Backend import Search,Analyse,flipkartReviewAnalyse,amazonReviewAnalyse,amazon,flipkart
# import bs4
from fake_headers import Headers
import os

app = Flask(__name__)

from flask import Flask,request,url_for,redirect,render_template
import pickle

app= Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("login.html")
database = {'user' : '123','admin':'admin123','Suresh':'123'}

@app.route('/form_login', methods=['POST','GET'])
def login():
    name1 = request.form['username']
    pwd = request.form['password']

    if name1 not in database:
        return render_template('login.html', info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
            return render_template('index1.html',name=name1)

# if __name__ =='__main__':
#     app.run()


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        # Get the product name from the form
        if(request.form["product_name"]):
            product_name = request.form.get("product_name")
            fp="static/Page/Plot.png"
            if(os.path.exists(fp)):
                os.remove(fp)
        # Call the search function with the product name
            Search(product_name,1)

            with open("Data.json",'r+') as f:
                js=json.load(f)
            return render_template('index.html', data=js,page=1,s=product_name)
        # else:
        #     return render_template('index.html')
    else:
        # Render the initial HTML form
        return render_template('index1.html')
    
@app.route('/<int:page>',methods=['GET','POST'])
def navigate(page):
    if request.method == 'POST':
        # Get the product name from the form
        if(request.form["Page"]):
            # product_name = request.form.get("product_name")
            # fp="static/Page/Plot.png"
            # if(os.path.exists(fp)):
            #     os.remove(fp)
            product_name=request.form.get('Page')
        # Call the search function with the product name
            Search(product_name,page)

            with open("Data.json",'r+') as f:
                js=json.load(f)
            p=page+1
            return render_template('index.html', data=js,page=p,s=product_name)
    else:
        # Render the initial HTML form
        return redirect("/")

@app.route("/analyse",methods=['POST','GET']) 
def page():
    if(request.method=='POST'):
        # fp="static/Page/Plot.png"
        # if(os.path.exists(fp)):
        #     os.remove(fp)
        Analyse()
        # with open("Data.json",'r+') as f:
        #     js=json.load(f)
        return render_template('Stats.html')
    else:
        return redirect("/")

@app.route("/aproductanalyse",methods=['GET','POST'])
def aproduct():
    if request.method=='POST':
        ASIN=request.form.get("ProductAnalyse")
        sentiment=amazonReviewAnalyse(ASIN)
        return render_template('Product.html',Data=sentiment)
    else:
        return redirect("/")
@app.route("/fproductanalyse",methods=['GET','POST'])
def fproduct():
    if request.method=='POST':
        FSN=request.form["ProductAnalyse"]
        sentiment=flipkartReviewAnalyse(FSN)
        return render_template('Product.html',Data=sentiment)
    else:
        return redirect("/")

@app.route("/compare",methods=["GET","POST"])
def compare():
    if(request.method=='POST'):
        Products=request.form.getlist("Product")
        f=1
        a=1
        if('flipkart'in Products[0]):
            flipkart(Products[0],f)
            f+=1
        if('flipkart' in Products[1],):
            flipkart(Products[1],f)
            f+=1
        if('amazon' in Products[0]):
            amazon(Products[0],a)
            a+=1
        if('amazon' in Products[1]):
            amazon(Products[1],a)
            a+=1
        with open("Data1.json",'r+') as f1:
                file1=json.load(f1)
        with open("Data2.json",'r+') as f2:
                file2=json.load(f2)
        return render_template('Compare.html',p1=file1,p2=file2)
    else:
        return redirect("/")


@app.route("/download",methods=["GET","POST"])
def download():
    path="Data.json"
    return send_file(path,as_attachment=True)


if __name__ == '__main__':
    app.run(debug=False,host ='0.0.0.0')
