# Import the Flask class from the flask module
from flask import Flask, jsonify

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__) #Here we initializate the Flask class

# Define a route for the root URL ("/")
@app.route("/")
def home():
    # Function that handles requests to the root URL
    #return "Hello, World!" #without returning a dictionary, it returns text/html (see with curl)
    # Create a dictionary to return as a response
    return {"message": "Hello World"} # it returns application/json (see with curl)

'''
    -To run in the terminal: flask --app server --debug run

    After running, we should be able to use the CURL command on localhost:5000/

    Note that the terminal is already running the server, you can use the 'Split Terminal' button to split the terminal
     and run the following command in the second tab.
            
            curl -X GET -i -w '\n' localhost:5000
            
            The -X argument specifies the GET command, and the -i argument displays the header from the response.

    Note: Kindly verify the presence of the Server.py file in the /home/project/lab directory 
    to prevent encountering a connection refusal error.
'''
