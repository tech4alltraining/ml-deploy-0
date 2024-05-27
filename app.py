# Import the Flask class from the flask module
from flask import Flask, request, render_template
import numpy as np
import pickle
# Create an instance of the Flask class
app = Flask(__name__)
# Register a route
@app.route('/')
def home():
    return render_template('index.html')


# Load the trained model
with open('iris_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/iris_flower', methods=['GET','POST'])
def iris_flower():
    # Define the label mapping
    label_mapping = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    if request.method == 'GET':
        return render_template('iris.html', prediction=None)
    if request.method == 'POST':
        sepal_length = float(request.form['sepalLength'])
        sepal_width = float(request.form['sepalWidth'])
        petal_length = float(request.form['petalLength'])
        petal_width = float(request.form['petalWidth'])

        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction_idx = model.predict(features)[0]
        prediction = label_mapping[prediction_idx]
    return render_template('iris.html', prediction=prediction, features = features[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)