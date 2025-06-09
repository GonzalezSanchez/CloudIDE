'''
Hands-on Lab: Building an API with Flask: Route Creation, Error Handling, and HTTP Requests
    Step 1: Set response status code
    Step 2: Process input arguments
    Step 3: Add dynamic URLs
    Step 4: Parse JSON from Request body
    Step 5: Add error handlers
'''

#Step 5: Add error handlers

'''
In this final part of the lab,
you will add application level global handlers to handle errors like 404 (not found) and 500 (internal server error).
Recall from the video that Flask makes it easy to handle these global error handlers using the errorhandler() decorator.

If you make an invalid request to the server now, Flask will return an HTML page with the 404 error. Something like this:

Command:
    curl -X POST -i -w '\n' http://localhost:5000/notvalid

Response:
    HTTP/1.1 404 NOT FOUND
    Server: Werkzeug/2.2.2 Python/3.7.16
    Date: Sun, 01 Jan 2023 23:21:54 GMT
    Content-Type: text/html; charset=utf-8
    Content-Length: 207
    Connection: close
    <!doctype html>
    <html lang=en>
    <title>404 Not Found</title>
    <h1>Not Found</h1>
    <p>The requested URL was not found on the server. If you entered the URL manually, please check your spelling and try again.</p>

This is great, but you want to return a JSON response for all invalid requests.
'''


#Tasks
'''
Create a method called api_not_found with the @app.errorhandler decorator.
This method will return a message of API not found
with an HTTP status code of 404 whenever the client requests a URL 
that does not lead to any endpoints defined by the server.

Hint
Use the @app.errorhandler decorator and pass in the HTTP code of 404.

You can use the following code as your starting point:
    {insert errorhandler decorator here}({insert error code here})
    def {insert method name here}(error):
        return {"message": "{insert error message here}"}, {insert error code here}
'''

@app.errorhandler(404)
def api_not_found(error):
    # This function is a custom error handler for 404 Not Found errors
    # It is triggered whenever a 404 error occurs within the Flask application
    return {"message": "API not found"}, 404


'''
You can test the endpoint with the following CURL command.
Ensure that the server is running in the terminal, as in the previous steps.
    curl -X POST -i -w '\n' http://localhost:5000/notvalid

You should see an output similar to the one below. Note the status of 404, Content-Type of application/json, and JSON output message of API not found:
    HTTP/1.1 404 NOT FOUND
    Server: Werkzeug/2.2.2 Python/3.7.16
    Date: Sun, 01 Jan 2023 23:25:35 GMT
    Content-Type: application/json
    Content-Length: 33
    Connection: close
    {
    "message": "API not found"
    }

Note that the server no longer returns HTML but JSON as required.

Similarly you can add a global Error Handler for 500 (internal server error) also.

You can register a global error handler in Flask for any unhandled exceptions by using:
    @app.errorhandler(Exception)
    def handle_exception(e):
        return {"message": str(e)}, 500

This tells Flask to catch any unhandled Exception raised anywhere in your app and route it to this handler,
returning a 500 Internal Server Error response with the error message.

You can deliberately raise an exception to test the global handler.
    @app.route("/test500")
    def test500():
        raise Exception("Forced exception for testing")

Then run this curl command in your terminal:
    curl http://localhost:5000/test500

You should see a response like:
    {
    "message": "Forced exception for testing"
    }
'''
