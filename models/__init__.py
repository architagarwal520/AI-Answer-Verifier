from flask import Flask 
from pyrebase import pyrebase



app = Flask(__name__)
app.config['SECRET_KEY']='a0e5afdbfeaea4959fe59f99f585d7a6'

config = {
  "apiKey": "AIzaSyBVrFHPJsViH2_svVfFJeMA4p-aZvl_Ua8",
  "authDomain": "ai-answer-verifier-master.firebaseapp.com",
  "databaseURL": "https://ai-answer-verifier-master.firebaseio.com",
  "projectId": "ai-answer-verifier-master",
  "storageBucket": "ai-answer-verifier-master.appspot.com",
  "messagingSenderId": "333164553539",
  "appId": "1:333164553539:web:e8aa6af643d4508bb47bf6",
  "measurementId": "G-MELWYDVM9X"
}


firebase = pyrebase.initialize_app(config=config)
db = firebase.database()


auth=firebase.auth()



from models import routes