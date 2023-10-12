from flask import Flask, render_template, request, session, redirect
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'your_database_name'

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Connect to MySQL database
        conn = MySQLdb.connect(host=app.config['MYSQL_HOST'],
                               user=app.config['MYSQL_USER'],
                               password=app.config['MYSQL_PASSWORD'],
                               db=app.config['MYSQL_DB'])

        # Create cursor
        cursor = conn.cursor()

        # Execute query
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))

        # Fetch one record
        user = cursor.fetchone()

        # Close cursor and connection
        cursor.close()
        conn.close()

        # Check if user exists in database
        if user:
            # Set session variable
            session['loggedin'] = True
            session['id'] = user[0]
            session['username'] = user[1]

            # Redirect to home page
            return redirect('/home')
        else:
            # Show error message
            return render_template('login.html', error='Invalid username or password')

    # Show login form
    return render_template('login.html')

# Home route
@app.route('/home')
def home():
    # Check if user is logged in
    if 'loggedin' in session:
        # Show home page
        return render_template('home.html', username=session['username'])
    else:
        # Redirect to login page
        return redirect('/')

# Logout route
@app.route('/logout')
def logout():
    # Clear session variables
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)

    # Redirect to login page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
