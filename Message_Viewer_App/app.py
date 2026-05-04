from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Fetching the message from K8s Environment Variable
    msg = os.getenv('APP_MESSAGE', 'Default: Local Development')
    APP_MESSAGE_PASSWORD = os.getenv('APP_MESSAGE_PASSWORD', 'No Password Found') 
    return render_template('index.html', message=msg, password=APP_MESSAGE_PASSWORD)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)