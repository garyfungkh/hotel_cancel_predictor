from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hotel():
	
	param_hotel = request.form.get("hotel_type")
	param_month = request.form.get("arrival_month")
	param_num = request.form.get("number_of_people")

	if param_hotel is None:
		return "Please provide hotel type"
	if param_month is None:
		return "Please provide arrival month"
	if param_num is None:
		return "Please provide number of resident"
	
	
	import pickle
	import numpy as np

	with open('exported_one_hot.pickle', 'rb') as fp:
		enc = pickle.load(fp)

	with open('exported_classifier.pickle', 'rb') as fp:
		classifier = pickle.load(fp)
	
	hotel_feature = enc.transform([['City Hotel']]).toarray()
	month_feature = (int(param_month)>= 6) and (int(parm_month) <=8)
	
	features = np.hstack([
	hotel_feature,
	np.array([[month_feature]]),
	np.array([[param_num]])
	
	])
	if classifier.predict(features):
		return 'will not cancel'
	else:
		return 'will cancel'

