from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-python', methods=['POST'])
def run_python():
    code = request.json.get('code')
    try:
        # Safely execute Python code
        output = subprocess.run(['python3', '-c', code], capture_output=True, text=True, check=True)
        return jsonify({'output': output.stdout})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.stderr}), 400

if __name__ == '__main__':
    app.run(debug=True)