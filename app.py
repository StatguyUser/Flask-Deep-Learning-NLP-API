####Dependencies
#1) Python 3
#2) flask, numpy, keras, tensorflow, pickle, logging
#these libraries can be installed one after another by typing library name after the command 'pip install'
#for example: pip install flask

#####Save model file and tokenizer pickle file in a single folder
#model.json
#model.h5
#tokenizer.pickle

#navigate to the folder which has app.py file in your computer and type below command and press enter to initialize the API
#python app.py

#call api by passing text after text = in below command to get the desired label for text
#http://localhost:5000/predict?text=

import os
from flask import jsonify
from flask import request
from flask import Flask
import numpy as np

from keras.models import model_from_json
from keras.models import load_model
from keras.preprocessing.text import Tokenizer, text_to_word_sequence
from keras.preprocessing.sequence import pad_sequences

import tensorflow as tf

import pickle

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

np.random.seed(1337)

graph = tf.get_default_graph()


#star Flask application
app = Flask(__name__)

#Load model
path = 'C:/Users/user/Downloads/Model/'
json_file = open(path+'/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
keras_model_loaded = model_from_json(loaded_model_json)
keras_model_loaded.load_weights(path+'/model.h5')
print('Model loaded...')


#load tokenizer pickle file
with open(path+'/tokenizer.pickle', 'rb') as handle:
    tok = pickle.load(handle)

def preprocess_text(texts,max_review_length = 100):
    #tok = Tokenizer(num_words=num_max)
    #tok.fit_on_texts(texts)
    cnn_texts_seq = tok.texts_to_sequences(texts)
    cnn_texts_mat = pad_sequences(cnn_texts_seq,maxlen=max_review_length)
    return cnn_texts_mat

# URL that we'll use to make predictions using get and post
#@app.route('/predict',methods=['GET','POST'])
@app.route('/predict',methods=['POST'])

def predict():
    text = request.args.get('text')
    x = preprocess_text([text])
    with graph.as_default():
        y = int(np.round(keras_model_loaded.predict(x)))
        if y == 1:
            return jsonify({'prediction': "Positive"})
        else:
            return jsonify({'prediction': "Negative"})


if __name__ == "__main__":
    # Run locally
    app.run(debug=False)

