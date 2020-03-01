from flask import Flask

app = Flask(__name__)

## POST -> recieves data
## GET -> sends data

#POST /store data: {name}

@app.route('/store', methods=['POST'])
def Create_Store():
    pass

@app.route('/store/<string:name>') # 'https://0.0.0.0:5000/store/some_name'
def get_stores(name):
    pass

@app.route('/store') # 'https://0.0.0.0:5000/store/some_name'
def get_store():
    pass

# @app.route('/')
# def home():
#     return 'hello, world'

app.run(port=1234)
