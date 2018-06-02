# Flask-Deep-Learning-NLP-API

#### This is built for windows 10

Flask API to productize a document classification model. Classification model was built using Keras with tensorflow backend.
Make sure to install all dependencies, which are listed below
1) Python 3
2) flask, numpy, keras, tensorflow, pickle, logging.

We will need the checkpointed exported model .json and .h5 extension files.

Also, we will need the original tokenizer used during model training process.

To initialize api, edit the api.py file and provide path for folder where model and tokenizer are saved.

In the command line in windows, navigate to folder where app.py is saved locally. in the command line, type `python app.py` to launch the API.

To access API for prediction purpose, URL is `http://localhost:5000/predict?text=`. Prediction text can be specified afterthis line. Below is an example of how to do this using `requests` library in Python using `post` method. Output will be in the form of JSON.

import requests

example_text = "I bought this product and its faulty. Feels like wasteage of money and time. I am not satisfied and want my money back. I will not recomment this."

requests.post('''http://localhost:5000/predict?text='''+example_text)
