from flask import Flask, jsonify

app = Flask(__name__)

## POST -> recieves data
## GET -> sends data

stores = [
    {
        'name': 'ganga raju kirana kottu',
        'items': [
            {
                'id': 1,
                'name': 'santoor soap',
                'cost': 15
            }
        ]
    }
]


# POST /store data: {name}

@app.route('/store', methods=['POST'])
def Create_Store():
    pass


@app.route('/store/<string:name>')  # 'https://0.0.0.0:5000/store/some_name'
def get_store(name):
    pass


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    pass


@app.route('/store/<string:name>/item')
def get_item_in_store():
    pass


@app.route('/')
def home():
    return 'hello, world'


app.run(port=1234)
