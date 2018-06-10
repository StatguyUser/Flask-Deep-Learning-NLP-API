# Flask-Deep-Learning-NLP-API

#### This is built for windows 10

Flask API to productize a document classification model. Classification model was built using Keras with tensorflow backend.
Make sure to install all dependencies, which are listed below
1) `Python 3`
2) `flask`, `numpy`, `keras`, `tensorflow`, `pickle`, `logging`.

We will need the checkpointed exported model .json and .h5 extension files. We will also need the original tokenizer used during model training process.

To initialize api, edit the `api.py` file and provide path for folder where model and tokenizer are saved. In the command line in windows, navigate to folder where app.py is saved locally. in the command line, type `python app.py` to launch the API.

To access API for prediction purpose, URL is `http://localhost:5000/predict?text=`. Prediction text can be specified afterthis line. Below is an example of how to do this using `requests` library in Python using `post` method. Output will be in the form of JSON.

`import requests`

`example_text = "A complete Bust: This game requires quicktime 5.0 to work...if you have a better version of quicktime (I have 7.5), it will ask you to install the quicktime available on the CD...if you click no, it will not let you play. So, I begrudgingly clicked yes on the third try, and it installed quicktime 5, THEN it tells me to please install the quicktime available on the disc. It KEPT telling me that, even after I uninstalled my version of quicktime 7.5, and reinstalled Barbie Rapunzel and quicktime 5. Very frustrating, and the game absolutely will not work for me. It keeps telling me over and over, to install quicktime 5, tho I've been through the installation process repeatedly. It is NOT my "operating system limitations". This is a brand new computer...merely weeks old with all the state of the art contraptions."`

`requests.post('''http://localhost:5000/predict?text='''+example_text)`

Corresponding model files are in my other repo https://github.com/newbiestatguy/Amazon-Review-Classification_DeepLearning

Feel free to reach out!!
