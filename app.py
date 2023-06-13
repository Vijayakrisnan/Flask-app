
import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__,template_folder='templates')
model = pickle.load(open("model.pkl", 'rb'))


@app.route('/')
def index():
    return render_template(
        'index.html',
        data=[{'gender': 'Gender'}, {'gender': 'female'}, {'gender': 'male'}])


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    input_data = list(request.form.values())
    if int(input_data[0]) & int(input_data[3]) & input_data[2].isdigit() == True:
        pass
    else:
        print(ValueError)

    if input_data[1] == 'female':
        input_data[1] = 0
    elif input_data[1] == 'male':
        input_data[1] = 1
    else:
        print(ValueError)




    input_values = [x for x in input_data]
    arr_val = [np.array(input_values)]
    prediction = model.predict(arr_val)
    output = round(prediction[0], 3)
    return render_template('index.html', prediction_text=" The predicted insurance charges is {}".format(output),
                           data=[{'gender': 'Gender'}, {'gender': 'female'}, {'gender': 'male'}])


if __name__ == '__main__':
    app.run(debug=True)