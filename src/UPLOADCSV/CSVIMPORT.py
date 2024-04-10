from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file_path = request.json.get('filePath')

    if not file_path:
        return jsonify({'success': False, 'message': 'No file path provided'}), 400
    print(f"Received file path: {file_path}")
    if os.path.isfile(file_path):
        return jsonify({'success': True, 'message': 'File path received and file exists'}), 200
    else:
        return jsonify({'success': False, 'message': 'File does not exist at the provided path'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=6002, host="0.0.0.0")
