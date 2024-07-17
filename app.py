from flask import Flask,render_template,request
import pickle
import os
#import joblib

class EuclideanDistance:
    # Define the custom class as it was during the training
    def __init__(self, *args, **kwargs):
        pass
    
        
app = Flask(__name__)
# model loading
model_path = os.path.join('Iris Flower Classification', 'knnmodel.pkl')
#model = joblib.load(open('P:/nbn/Placements/CipherByte Technologies/CBTCIP-master/Iris Flower Classification/knnmodel.pkl','rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())

@app.route('/predict', methods =['POST','GET'])
def predict():
    
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])
    result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)