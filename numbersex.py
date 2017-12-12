from flask import Flask
from flask.ext.pymongo import PyMongo, pymongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'connect_to_mongo'
app.config['MONGO_URI'] = 'mongodb://gf1721:Garden12@ds135916.mlab.com:35916/connect_to_mongo'

mongo = PyMongo(app)

@app.route('/')
def index():
    numbers = mongo.db.numbers
    results = numbers.find({'number': {'$lt':8}})
    
    output = ''
    for r in results:
        output += r['name'] + ' - ' + str(r['number']) + '<br>'
    
    return output

@app.route('/add')
def add():
    number = mongo.db.numbers
    number.insert({'name':'one', 'number':1})
    number.insert({'name':'two', 'number':2})
    number.insert({'name':'three', 'number':3})
    number.insert({'name':'four', 'number':4})
    number.insert({'name':'five', 'number':5})
    number.insert({'name':'six', 'number':6})
    number.insert({'name':'seven', 'number':7})
    number.insert({'name':'eight', 'number':8})
    number.insert({'name':'nine', 'number':9})
    
    return 'Added numbers'
    
    
if __name__ == '__main__':
    app.run(debug=None)