from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Mock database: In a real application, replace this with actual database logic
users = {
    'john': {'password': 'johnpassword', 'age': 30, 'location': 'New York'},
    'alice': {'password': 'alicepassword', 'age': 25, 'location': 'Los Angeles'}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return "Signup Page"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Authenticate the user
        user = users.get(username)
        if user and user['password'] == password:
            # Store the username in session
            session['username'] = username

            # Redirect to the user dashboard
            return redirect(url_for('dashboard', username=username))
        else:
            # Authentication failed
            return "Invalid credentials. Please try again."

    return render_template('login.html')



@app.route('/dashboard/<username>')
def dashboard(username):
    # Ensure the user is logged in
    if 'username' not in session or session['username'] != username:
        return redirect(url_for('login'))

    # Fetch user data from the mock database
    user_data = users.get(username)
    if not user_data:
        return "User not found."

    # Render the dashboard with user data
    return render_template('dashboard.html', user=user_data)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

