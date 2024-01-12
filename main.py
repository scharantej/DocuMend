 
# Import necessary libraries
from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)

# Define the route for the main page
@app.route('/')
def index():
    # Render the index.html file
    return render_template('index.html')

# Define the route for handling the form submission
@app.route('/greet', methods=['POST'])
def greet():
    # Get the user's name from the form data
    name = request.form['name']

    # Generate a personalized greeting message
    greeting = f"Hello, {name}! Welcome to our website."

    # Render the greeting.html file with the greeting message
    return render_template('greeting.html', greeting=greeting)

# Run the app
if __name__ == '__main__':
    app.run()
