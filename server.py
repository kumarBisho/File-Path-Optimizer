
# Flask backend for directory path simplification with CORS and error handling
import os
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

def split_string(path, sep):
    temp = []
    path += sep
    n = len(path)
    curr = ''
    for i in range(n):
        if path[i] != sep:
            curr += path[i]
        else:
            if curr:
                temp.append(curr)
            curr = ''
    return temp

def simplify_path(path):
    ans = []
    temp = split_string(path, '/')
    for t in temp:
        if t == '.' or t == '/':
            continue
        elif t == '..':
            if ans:
                ans.pop()
        else:
            ans.append(t)
    if not ans:
        return '/'
    return '/' + '/'.join(ans)

@app.route('/simplify', methods=['POST'])
def simplify():
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    data = request.get_json()
    if not data or 'path' not in data:
        return jsonify({'error': 'Missing "path" in request'}), 400
    path = data['path']
    try:
        simplified = simplify_path(path)
        return jsonify({'simplified': simplified})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return 'Directory Path Simplifier API is running.'

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
