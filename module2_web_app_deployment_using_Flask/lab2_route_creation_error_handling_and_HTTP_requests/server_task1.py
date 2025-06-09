'''
Hands-on Lab: Building an API with Flask: Route Creation, Error Handling, and HTTP Requests
    Step 1: Set response status code
    Step 2: Process input arguments
    Step 3: Add dynamic URLs
    Step 4: Parse JSON from Request body
    Step 5: Add error handlers
'''
#Step 1: Set response status code

# Import the Flask class from the flask module
from flask import Flask, make_response
# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)
# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world"

    r'''
    to run the server from the terminal:
        flask --app server2 --debug run

    Then use the CURL command with localhost:5000/. Note that the terminal is running the server.
    So, use the Split Terminal button to split the terminal and run the following command in the second tab.
        curl -X GET -i -w '\n' localhost:5000

    If the command prompt is long, you can shorten it:
        export PS1="[\[\033[01;32m\]\u\[\033[00m\]: \[\033[01;34m\]\W\[\033[00m\]]\$ "
    '''


r'''
Step 1: 
    You can also set the return status explicitly. There are two ways to do this:
        -   Send a tuple back with the message
        -   Use the make_response() method to create a custom response and set the status

    Taks:    
        Task 1. Send custom HTTP code back with a tuple.
                Create a new method named no_content with the @app.route decorator and URL of /no_content.
                The method does not have any arguments. Return a tuple with the JSON message No content found.

            You can test the endpoint with the following CURL command:
                curl -X GET -i -w '\n' localhost:5000/no_content

            You should see an output similar to the following. Note the status of 204 and the Content-Type of application/json.
            Note that even though you returned a JSON message, it is not sent back to the client as 204.
            By default, nothing is returned.
                HTTP/1.1 204 NO CONTENT
                Server: Werkzeug/2.2.2 Python/3.7.16
                Date: Wed, 28 Dec 2022 19:49:18 GMT
                Content-Type: application/json
                Connection: close

            Why Use 204?
                The 204 No Content status is used in REST APIs when a request succeeds but no data needs to be returned.
                For example:
                    -   After deleting a resource (e.g., a user), the server confirms success without sending the deleted data.
                    -   When confirming an action (e.g., updating settings) without additional information.
                    -   Here we are returning a JSON message. But because we are telling the client via the status code 204 that no content 
                        will be returned, most HTTP clients will ignore the body. If you need to show a message, use status code 200
                    -   Send custom HTTP code back with the make_response() method.The make_response() method in Flask is used to create 
                            a full HTTP response object manually, giving you more control over the response than just returning a value or a tuple.
'''


#Step 1. Set response status code
#Step 1. Task 1.

#{insert @app decorator}
@app.route("/no_content")
#def {insert method name}():
def no_content():
    '''
    return 'No content found' with a status of 204
    Returns:
        string: No content found
        status code: 204
    '''
    #return ({insert dictionary here}, {insert HTTP code here})
    return ({"message": "No content found"}, 204)
    '''
    no need to put a message because it will not be shown
        Option 1: Stick with 204, but don't include a body
            return '', 204
        Option 2: Use 200 OK or 404 Not Found if a message matters
            return {"message": "No content found"}, 200  # or 404 if it's an error
    Use a different status code (rather than 204) if you need to send a message.
    '''

r'''
Step 1 (vervolgd):
    Task 2. Create a second method named index_explicit with the @app.route decorator and a URL of /exp.
        The method does not have any arguments. Use the make_response() method to create a new response. Set the status to 200.
        You can test the endpoint with the following CURL command:
            curl -X GET -i -w '\n' localhost:5000/exp

        You should see an output similar to the one given below. Note the status of 200,
        Content-Type of application/json, and JSON output of {"message": "Hello World"}:
            HTTP/1.1 200 OK
            Server: Werkzeug/2.2.2 Python/3.7.16
            Date: Wed, 28 Dec 2022 19:55:46 GMT
            Content-Type: application/json
            Content-Length: 31
            Connection: close
            {
            "message": "Hello World"
            }
'''


#Step 1. Task 2.

#{insert @app decorator}
@app.route('/exp')
#def {insert method name here}:
def index_explicit():
    '''
    return 'Hello World' message with a status code of 200
    Returns:
        string: Hello World
        status code: 200
    '''
    #resp = make_response({insert ditionary here})
    resp = make_response({'message': 'Hello world'})
    #we could use #resp = make_response(jsonify({'message': 'Hello world'})) #but dont forget to import jsonify

    #resp.status_code = {insert status code here}
    resp.status_code = 200
    return resp
