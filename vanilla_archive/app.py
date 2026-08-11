import os
from flask import Flask, send_from_directory, jsonify
from draw_logic import draw_all_winners

app = Flask(__name__, static_folder='.', static_url_path='')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(BASE_DIR, filename)

# SECRET ADMIN PORTAL URL
@app.route('/admin_secure_portal_777')
def admin_portal():
    return send_from_directory(BASE_DIR, 'admin.html')

@app.route('/api/reset_draw', methods=['POST'])
def reset_draw():
    master_csv = os.path.join(BASE_DIR, 'master_data.csv')
    try:
        results = draw_all_winners(master_csv, BASE_DIR)
        return jsonify({"success": True, "details": {k: len(v) for k, v in results.items()}})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    print("\n" + "="*50)
    print("SERVER RUNNING")
    print(f"MAIN PORTAL: http://127.0.0.1:5000/")
    print(f"SECURE ADMIN: http://127.0.0.1:5000/admin_secure_portal_777")
    print("="*50 + "\n")
    app.run(debug=True, port=5000)
