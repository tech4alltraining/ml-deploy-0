# Import the Flask class from the flask module
from flask import Flask, render_template
# Create an instance of the Flask class
app = Flask(__name__)
# Register a route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/iris_flower', methods=['POST'])
def iris_flower():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(data['features'])])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)