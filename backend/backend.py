from flask import Flask,request,jsonify

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

@app.route('/submit',methods=['POST'])
def submit():
    form_data = dict(request.json)
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
    return jsonify(data)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9001,debug=True)
