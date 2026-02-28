from flask import Flask, jsonify, request
from flask_cors import CORS
from supabase import create_client, Client

SUPABASE_URL = "https://cooqztopqjjfgshnvteo.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNvb3F6dG9wcWpqZmdzaG52dGVvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5ODkyMzYsImV4cCI6MjA4NzU2NTIzNn0.-Bgpp_Kx_IyMIAGuy7yVqqdwOp8s4hW9L--ad2XXGyY"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
app = Flask(__name__)
CORS(app)

@app.route('/tasks', methods=['GET'])
def get_task(): 
	respond = supabase.table('tasks').select('*').execute()
	return jsonify(response.data)

@app.route('/tasks', methods=['POST'])
def add_task ():
	data = request.get_json()

	response = supabase.table('tasks').insert({'task': data['task']}).execute()

	response = supabase.table('tasks').select('*').execute()
	return jsonify(response.data)

if __name__ == '__main__':
	app.run(debug=True)


