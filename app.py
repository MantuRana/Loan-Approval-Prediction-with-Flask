from flask import Flask, render_template,request
import pickle
import numpy as np

model = pickle.load(open('model2.pkl','rb'))

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict_placement():
    age = int(request.form.get('age'))
    gender = int(request.form.get('gender'))
    income = int(request.form.get('income'))
    credit = int(request.form.get('credit'))
# prediction
    result = model.predict(np.array([age, gender, income, credit]).reshape(1,4))
    # return str(result)
    if result[0] == 0:
        result = 'Congrates🪄🪄 Loan Approved😀😀'
    else:
        result = 'Not Approved😔😔'
    return render_template('index.html', result = result)




if __name__ == '__main__':
    app.run(debug=True)
