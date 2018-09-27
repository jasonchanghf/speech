from flask import Flask

app=Flask(__name__)

@route('/')
def index():
    return 'hello'