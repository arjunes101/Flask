from flask import Flask, render_template, request
from datetime import datetime
from pymongo import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://arjunes101_db_user:*!hRu86lp1@cluster0.kqvmedk.mongodb.net/?appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['test']
collection = db['Flask_Tutorial']
app = Flask(__name__)
@app.route('/')
def home():
    days_of_week = datetime.today().strftime('%A')
    current_time = datetime.today()
    return render_template('index3.html', days_of_week=days_of_week, current_time=current_time)
@app.route('/submit',methods=['POST'])
def submit():
    form_data = dict(request.form)
    collection.insert_one(form_data)
    return 'Data submitted successfully!'
@app.route('/view',methods=['GET'])
def view():
    data = collection.find()
    data = list(data)
    for item in data:
     print(item)
     del item["_id"]
    data ={
        "data": data
    }
    return data
if __name__ == '__main__':
    app.run(debug=True)
