from flask import Flask
import time

app = Flask('app')

@app.route('/')
def home():
  return time.time()
