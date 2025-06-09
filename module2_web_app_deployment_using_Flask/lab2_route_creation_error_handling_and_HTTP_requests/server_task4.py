'''
Hands-on Lab: Building an API with Flask: Route Creation, Error Handling, and HTTP Requests
    Step 1: Set response status code
    Step 2: Process input arguments
    Step 3: Add dynamic URLs
    Step 4: Parse JSON from Request body
    Step 5: Add error handlers
'''

#Step 4: Parse JSON from Request body
'''
Let's create another RESTful API.
The client can send a POST request to http://localhost:5000/person with the person detail JSON as the body.
The server should parse the request for the body and then create a new person with that detail.
In your case, to create the person, simply add to the data list.
'''

#Tasks
'''
Create a method called add_by_uuid with the @app.route decorator. This method should be called when a client requests with the POST method for the /person URL. The method will not accept any parameter but will grab the person details from the JSON body of the POST request. The method returns:

The person’s id with an HTTP 200 status code if the person is successfully added to the data list.
A message "Invalid input parameter" with an HTTP 422 status code if the JSON body is missing or empty.

Hint
Ensure you import the request module from Flask.
You will use this to get the first name from the HTTP request.
'''

from flask import Flask, request

app = Flask(__name__)

'''
You can use the following code as your starting point.
In production code, you will put in some logic to validate the JSON coming in.
You would not want to store any random data coming from a client.
You can omit this validation for your simple use case.
'''

@app.route("/")
def index():
    return "Flask is working!" #Alvaro: to check if Flask is running
    #in the terminal -> curl http://localhost:5000/

@app.route("/person", methods=['POST'])
def create_person():
    # Get the JSON data from the incoming request
    new_person = request.get_json()
    # Check if the JSON data is empty or None
    if not new_person:
        # Return a JSON response indicating that the request data is invalid
        # with a status code of 422 (Unprocessable Entity)
        return {"message": "Invalid input, no data provided"}, 422
    # Proceed with further processing of 'new_person', such as adding it to a database
    # or validating its contents before saving it
    # Assuming the processing is successful, return a success message with status code 200 (Created)
    return {"message": "Person created successfully"}, 200

'''
You can test the endpoint with the following CURL command. Ensure that the server is running in the terminal as in the previous steps.
    curl -X POST -i -w '\n' \
  --url http://localhost:5000/person \
  --header 'Content-Type: application/json' \
  --data '{
        "id": "4e1e61b4-8a27-11ed-a1eb-0242ac120002",
        "first_name": "John",
        "last_name": "Horne",
        "graduation_year": 2001,
        "address": "1 hill drive",
        "city": "Atlanta",
        "zip": "30339",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff"
}'

You should see an output similar to the one given below. Note the status of 200, Content-Type of application/json, and JSON output of person with the first name Abdel:
    HTTP/1.1 200 OK
    Server: Werkzeug/2.2.2 Python/3.7.16
    Date: Sun, 01 Jan 2023 23:14:34 GMT
    Content-Type: application/json
    Content-Length: 56
    Connection: close
    {
    "message": "4e1e61b4-8a27-11ed-a1eb-0242ac120002"
    }

You can also test the case where you send an empty JSON to the endpoint by using the following command:
    curl -X POST -i -w '\n' \
    --url http://localhost:5000/person \
    --header 'Content-Type: application/json' \
    --data '{}'

The server should return a code of 422 with a message of Invalid input parameter.
    HTTP/1.1 422 UNPROCESSABLE ENTITY
    Server: Werkzeug/2.2.2 Python/3.7.16
    Date: Sun, 01 Jan 2023 23:15:54 GMT
    Content-Type: application/json
    Content-Length: 43
    Connection: close
    {
    "message": "Invalid input parameter"
    }
'''
