# IGNORE THIS FILE
from flask import Flask, render_template, session, request, jsonify
from flask_session import Session

def main():
    app = Flask(__name__, template_folder="templates")

    # Configure session (replace SECRET_KEY with a strong, random string)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SESSION_TYPE'] = 'filesystem'  # Use filesystem storage
    Session(app)  # Initialize session

    # @app.route('/')
    # def index():
    #     # Check if user is logged in (example)
    #     if 'username' in session:
    #         return f"Welcome back, {session['username']}!"
    #     else:
    #         return render_template('login.html')  # Render login page

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')  # Render login form on GET
        # else:  # Handle POST request for login form submission
        request_data = request.json
        username = request_data.get('username')
        print(username)

        # Implement your secure authentication logic here (replace with your logic)
        if username == 'valid_user':
            session['username'] = username
            print(session['username'])

            data = {"result": "Valid credentials"}
            return jsonify({'success': True, 'data': data}), 200
        else:
            data = {"result": "Invalid credentials"}
            return jsonify({'success': False, 'data': data}), 400

    @app.route('/success', methods=['GET', 'POST'])
    def success():
        if request.method == 'GET':
            return render_template('success.html')
        

    # Add more API routes for data fetching, manipulation, etc.

    app.run(debug=True, host="0.0.0.0", port=5007)
