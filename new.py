#Importing
from flask import Flask, render_template, request
#Interaction
app = Flask(__name__)
#Mapping
@app.route('/')
@app.route('/register')


#Inputs
def home():
    return render_template('register.html')
@app.route('/confirmation', methods=['POST','GET'])

def register():
    if request.method == "POST":
        n = request.form['name']
        c = request.form['city']
        p = request.form['Phone']
        return render_template('confirm.html', name=n, city=c, Phone=p)
#MAIN
if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=8080, debug=True)