from flask import *
import json
from pyspark import SparkContext, SparkConf


import csv

app = Flask(__name__)

with open('/Users/xiongzhuoran/Downloads/Final_project/myproject/X.csv','rb') as csvfile:
	reader = csv.DictReader(csvfile)
	model = [row for row in reader]
	print(model[0])

@app.route('/', methods=['GET','POST'])
def hello():
	if request.method == 'POST':
		return redirect(url_for('send'))
	return render_template('index.html')

@app.route('/send',methods=['GET','POST'])
def send():
	userID = None
	if request.method == 'POST':		
		userID = request.form['userID']
		Recommendation = model[int(userID)-1]
		return render_template('index.html',Recommendation=Recommendation)
	return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True)
