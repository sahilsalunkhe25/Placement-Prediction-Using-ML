from tkinter import Variable
from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app=Flask(__name__,template_folder='templates')
model=pickle.load(open('A:\MINI PROJECT\website\model1.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("PredictionWebsite.html")



@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(float(x)) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1],2)

    if output>str(0.5):
        return render_template('PredictionWebsite.html',pred='Probability of your placement is high🎉🎉') 
    else:
        return render_template('PredictionWebsite.html',pred='Probability of your placement is low.\n Keep working hard :)')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500)