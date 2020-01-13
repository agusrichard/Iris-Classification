import numpy as np
import pickle
from flask import render_template, request, Blueprint 
from flask_login import login_required
from . import main
from .forms import PredictionForm
from .classifier import make_prediction

@main.route('/')
@main.route('/home')
def home():
	return render_template('home.html')


@main.route('/dataset')
@login_required
def dataset():
	return render_template('dataset.html', title='Dataset')


@main.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
	form = PredictionForm()
	prediction = None
	if form.validate_on_submit():
		request_arr = [x for x in request.form.values()]
		arr = request_arr[1:-1] 
		arr = [float(x) for x in arr]
		arr = np.array(arr).reshape(1, -1)
		print("The array: ", arr)
		prediction = make_prediction(arr)
		
	return render_template('predict.html', title='Predict', form=form, prediction=prediction)
