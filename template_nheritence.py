#Importing
from flask import Flask, render_template
#Interaction
app = Flask(__name__)
#Mapping
@app.route('/')


#Inputs
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=8080, debug=True)