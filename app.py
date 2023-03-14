from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


inputs = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        input_ = request.form['input']
        inputs.append(input_)
        return str(len(inputs) - 1)


@app.route('/<int:index_>')
def get_input(index_):
    try:
        return inputs[int(index_)]
    except Exception:
        return ''


if __name__ == '__main__':
    app.run(port=5001)
