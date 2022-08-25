from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route('/')
def printHelloWorld():
    return '<h1>Hello World</h1>'

@app.route('/time')
def getCurrentTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=port)
    
    
  
