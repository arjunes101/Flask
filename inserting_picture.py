from flask import Flask, render_template
import os
app = Flask(__name__)
picFolder = os.path.join('static')
app.config['UPLOAD_FOLDER'] = picFolder
@app.route('/')
def first():
    pic = os.path.join(app.config['UPLOAD_FOLDER'],'laptop.jpg')
    return render_template('home1.html',user_pic=pic)
@app.route('/second')
def second():
    return "Welcome to the second page"
if __name__ == '__main__':
    app.run(debug=True)