import os
import lancedb
from flask import Flask, request, jsonify

app = Flask(__name__)
db = lancedb.connect('/mnt/data/lancedb')  # Adjust path as needed

# Create a sample table if it doesn't exist
try:
    db.create_table('example_table', schema={'id': 'INT', 'vector': 'VECTOR', metadata: 'TEXT'})
except Exception as e:
    print(f "Table creation skipped: {e}")
@app.route('/ingest', methods='POST')
def ingest_data():
    data = request.json
    db.insert('example_table', data)
    return jsonify { 'status': 'success'}

@app.route('/query', methods='GET')
def query_data():
    query = request.args.get('query')
    results = db.query('example_table', query)
    return jsonmy(results)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
