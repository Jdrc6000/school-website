from flask import Flask

app = Flask('app')

@app.route('/')
def home():
  return 'Hello, world!'
