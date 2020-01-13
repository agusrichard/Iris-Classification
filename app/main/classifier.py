import pickle
import os
from flask import current_app


def make_prediction(x):
	pth = os.path.join(current_app.root_path, 'estimator/finalized_model.sav')

	model = pickle.load(open(pth, 'rb'))

	prediction = model.predict(x)
	if prediction == 0:
		return "Iris Setosa"
	elif prediction == 1:
		return "Iris Virginica"
	else:
		return "Iris Versicolor"