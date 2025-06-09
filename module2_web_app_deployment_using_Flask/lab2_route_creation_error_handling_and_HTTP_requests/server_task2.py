'''
Hands-on Lab: Building an API with Flask: Route Creation, Error Handling, and HTTP Requests
    Step 1: Set response status code
    Step 2: Process input arguments
    Step 3: Add dynamic URLs
    Step 4: Parse JSON from Request body
    Step 5: Add error handlers
'''

#Step 2. Procss input arguments

from flask import Flask, make_response, request
app = Flask(__name__)

'''
It is common for clients to pass arguments in the URL. 
The lab provides a list of people with their id, first name, last name, and address information in an
object. Normally, this information is stored in a database, but you are using a hard coded list for your 
simple use case. This data was generated with Mockaroo.

The client will send in requests in the form of http://localhost:5000?q=first_name.
You will create a method that will accept a first_name as the input
and return a person with that first name.

This is the data[] for this Step:
'''
data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

r'''
Let's confirm that the data has been copied to the file. Copy the following code into the
'''
@app.route("/data")
def get_data():
    try:
        # Check if 'data' exists and has a length greater than 0
        if data and len(data) > 0:
            # Return a JSON response with a message indicating the length of the data
            return {"message": f"Data of length {len(data)} found"}
        else:
            # If 'data' is empty, return a JSON response with a 500 Internal Server Error status code
            return {"message": "Data is empty"}, 500
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not Found status code
        return {"message": "Data not found"}, 404

'''
The above code simply checks if the variable data exits.
    If it does not, the NameError is raised and an HTTP 404 is returned.
    If data exists and is empty, an HTTP 500 is returned.
    If data exists and is not empty, an HTTP 200 success message is returned.

Run a CURL command to confirm you get the success message back:
    curl -X GET -i -w '\n' localhost:5000/data

Expected result:
    HTTP/1.1 200 OK
    Server: Werkzeug/2.2.2 Python/3.7.16
    Date: Wed, 28 Dec 2022 20:51:56 GMT
    Content-Type: application/json
    Content-Length: 42
    Connection: close
    {
    "message": "Data of length 5 found"
    }
'''

'''
Your Tasks
Create a method called name_search with the @app.route decorator.
This method should be called when a client requests for the /name_search URL.
The method will not accept any parameter, however, will look for the argument q in the incoming request URL.
This argument holds the first_name the client is looking for.
The method returns:
    - Person information with a status of HTTP 200 if the first_name is found in the data
    - Message of Invalid input parameter with a status of HTTP 400 if the argument q is missing from the request
    - Message of Person not found with a status code of HTTP 404 if the person is not found in the data

    Hint
    Ensure you import the request module from Flask. You will use this to get the first name from the HTTP request.
       - from flask import request
'''

@app.route("/name_search")
def name_search():
    '''Find a person in the database.

    Returns:
        json: Person if found, with status of 200
        404: If not found
        400: If argument 'q' is missing
        422: If argument 'q' is present but invalid
   '''

    # Get the argument 'q' from the query parameters of the request
    query = request.args.get('q')

    # Check if the query parameter 'q' is missing
    if query is None:
        return {"message": "Query parameter 'q' is missing"}, 400

    # Check if the query parameter is present but invalid (e.g., empty or numeric)
    if query.strip() == "" or query.isdigit():
        return {"message": "Invalid input parameter"}, 422

    # Iterate through the 'data' list to look for the person whose first name matches the query
    for person in data:
        if query.lower() in person["first_name"].lower():
            # If a match is found, return the person as a JSON response with a 200 OK status code
            return person, 200

    # If no match is found, return a JSON response with a message indicating the person was not found and a 404 Not Found status code
    return {"message": "Person not found"}, 404

    '''
    You can test the endpoint with the following CURL command. 
        curl -X GET -i -w '\n' "localhost:5000/name_search?q=Abdel"

    You should see an output similar to the one given below.
    Note the status of 200, Content-Type of application/json, and JSON output of person with first name Abdel:
        HTTP/1.1 200 OK
        Server: Werkzeug/2.2.2 Python/3.7.16
        Date: Wed, 28 Dec 2022 21:14:31 GMT
        Content-Type: application/json
        Content-Length: 295
        Connection: close
        {
        "address": "2 Lake View Point",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
        "city": "Shreveport",
        "country": "United States",
        "first_name": "Abdel",
        "graduation_year": 1995,
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "last_name": "Duke",
        "zip": "71105"
        }

    Next, test that the method returns HTTP 422 if the argument q is invalid:
        curl -X GET -i -w '\n' "localhost:5000/name_search?q=123"
    or
        curl -X GET -i -w '\n' "localhost:5000/name_search?q="
    Note: Use HTTP 400 (Bad Request) when the required query parameter is missing.
    Use HTTP 422 (Unprocessable Entity) only if the parameter is present but has invalid or unacceptable content.

    You should see an output similar to the one given below.
    Note the status of 422, Content-Type of application/json, and JSON output of Invalid input parameter:
        HTTP/1.1 422 UNPROCESSABLE ENTITY
        Server: Werkzeug/2.2.2 Python/3.7.16
        Date: Wed, 28 Dec 2022 21:16:07 GMT
        Content-Type: application/json
        Content-Length: 43
        Connection: close
        {
        "message": "Invalid input parameter"
        }

    Finally, let's test the case where the first_name is not present in our list of people:
        curl -X GET -i -w '\n' "localhost:5000/name_search?q=qwerty"

    You should see an output similar to the one given below.
    Note the status of 404, Content-Type of application/json, and JSON output of Person not found:
        HTTP/1.1 404 NOT FOUND
        Server: Werkzeug/2.2.2 Python/3.7.16
        Date: Wed, 28 Dec 2022 21:17:28 GMT
        Content-Type: application/json
        Content-Length: 36
        Connection: close
        {
        "message": "Person not found"
        }
'''
