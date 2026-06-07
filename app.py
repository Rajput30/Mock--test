from flask import Flask, Response
import os

app = Flask(__name__)

@app.route('/')
def home():
    path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    return Response(content, mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=True)
