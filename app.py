from flask import Flask

app = Flask(__name__)   #Create a Flask application instance  

@app.route('/')   #Define a route for the root
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)