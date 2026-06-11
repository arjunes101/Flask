from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def home():
    days_of_week = datetime.today().strftime('%A')
    current_time = datetime.today()
    return render_template('index2.html', days_of_week=days_of_week, current_time=current_time)
@app.route('/submit',methods=['POST'])
def submit():
    form_data = request.form
    print(form_data)
    return form_data
if __name__ == '__main__':
    app.run(debug=True)
