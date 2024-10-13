from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_babel import Babel

app = Flask(__name__)
app.secret_key = 'your_secret_key'
babel = Babel(app)

# 定义语言列表
LANGUAGES = ['en', 'zh-tw']

# 默认语言
@app.route('/')
def index():
    return render_template('index.html')

@babel.localeselector
def get_locale():
    return session.get('lang', 'en')

@app.route('/set-language/<lang>', methods=['POST'])
def set_language(lang):
    if lang in LANGUAGES:
        session['lang'] = lang
    return jsonify({'status': 'success', 'lang': lang})

@app.route('/get-test', methods=['GET'])
def get_test():
    param = request.args.get('param', 'default')
    return jsonify({'message': f'GET request received with param: {param}'})

@app.route('/post-test', methods=['POST'])
def post_test():
    data = request.get_json()
    message = data.get('message', 'No message received')
    return jsonify({'message': f'POST request received with message: {message}'})

if __name__ == '__main__':
    app.run(debug=True,port=10000, host='0.0.0.0')
