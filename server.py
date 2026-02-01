from flask import Flask, request, jsonify, send_from_directory
import os
import sys

# Add tools directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'tools'))
from llm_client import OllamaClient

app = Flask(__name__, static_folder='ui', static_url_path='')
client = OllamaClient()

@app.route('/')
def home():
    # Serve index.html if it exists, otherwise simple string
    if os.path.exists(os.path.join(app.static_folder, 'index.html')):
        return send_from_directory(app.static_folder, 'index.html')
    return "<h1>B.L.A.S.T. Converter Active</h1><p>UI not yet built. Use POST /api/convert</p>"

@app.route('/api/convert', methods=['POST'])
def convert():
    data = request.json
    if not data or 'java_code' not in data:
        return jsonify({"error": "Missing 'java_code' in body"}), 400
    
    java_code = data['java_code']
    ts_code = client.convert(java_code)
    
    return jsonify({
        "ts_code": ts_code,
        "status": "success"
    })

@app.route('/api/save', methods=['POST'])
def save_file():
    data = request.json
    if not data or 'ts_code' not in data:
        return jsonify({"error": "Missing 'ts_code'"}), 400
    
    ts_code = data['ts_code']
    filename = data.get('filename', 'converted_test.spec.ts')
    
    # Save to a 'output' directory
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    file_path = os.path.join(output_dir, filename)
    with open(file_path, "w") as f:
        f.write(ts_code)
        
    return jsonify({
        "status": "success",
        "path": file_path,
        "message": f"File saved to {file_path}"
    })

if __name__ == '__main__':
    print("🚀 Server starting on http://localhost:5001")
    app.run(debug=True, port=5001)
