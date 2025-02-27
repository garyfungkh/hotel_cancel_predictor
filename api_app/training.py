from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

enc = OneHotEncoder()

enc.fit(df[['hotel']])

hotel_feature = enc.transform(df[['hotel']]).toarray()

is_summer_feature = df['arrival_date_month'].isin([6,7,8])

num_of_ppl_feature = df['children'].fillna(0) + df['adults'].fillna(0)

X = pd.concat([pd.DataFrame(hotel_feature), is_summer_feature, num_of_ppl_feature], axis=1).values
y= df['is_canceled']

classifier = RandomForestClassifier()

classifier.fit(X, y)



import pickle

with open('exported_one_hot.pickle', 'wb') as fp:
    pickle.dump(enc, fp)

with open('exported_classifier.pickle', 'wb') as fp:
    pickle.dump(classifier, fp)
	
enc.transform([['City Hotel']]).toarray()