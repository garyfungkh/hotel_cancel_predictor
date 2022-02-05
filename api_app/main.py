from flask import Flask
app = Flask(__name__)

@app.route('/')
def hotel():
	param_hotel = 'City Hotel'
	param_month = '2'
	param_num = 12
	
	import pickle
	import numpy as np

	with open('exported_one_hot.pickle', 'wb') as fp:
		pickle.load(enc, fp)

	with open('exported_classifier.pickle', 'wb') as fp:
		pickle.load(classifier, fp)
	
	hotel_feature = enc.transform([['City Hotel']]).toarray()
	month_feature = (int(param_month)>= 6) and (int(parm_month) <=8)
	
	features = np.hstack([
	hotel_feature,
	np.array([[month_feature]]),
	np.array([][param_num])
	
	])
	return classifier.predict(feature)

