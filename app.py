from flask import Flask,render_template,request,jsonify
import datetime
import pickle
import numpy as np


app= Flask(__name__)



@app.route('/',methods=['GET','POST'])
def forecast():
    if request.method=="POST":


        startdate = datetime.datetime.strptime( request.form['sdate'],'%Y-%m-%d')
        enddate = datetime.datetime.strptime(request.form['edate'], '%Y-%m-%d')
        loadmodel = pickle.load(open('sarimax.pkl', 'rb'))
        results=np.expm1(loadmodel.predict(start=startdate, end=enddate, dynamic=False)).sum()
        results=str(round(results))
        return ("REVENUE FORECASTING FOR GIVEN DATE RANGE IS : "+results)

    return render_template('index.html')






if __name__=="__main__":
    app.run(debug=True)


