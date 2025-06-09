'''
Hands-on Lab: Building an API with Flask: Route Creation, Error Handling, and HTTP Requests
    Step 1: Set response status code
    Step 2: Process input arguments
    Step 3: Add dynamic URLs
    Step 4: Parse JSON from Request body
    Step 5: Add error handlers
'''

#Step 3: Add dynamic URLs

from flask import Flask, make_response, request
app = Flask(__name__)

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

'''
An important part of back-end programming is creating APIs.
An API is a contract between a provider and a user.
It is common to create RESTful APIs that can be called by the front end or other clients.
In a REST based API, the resource information is sent as part of the request URL.
For example, with your resource or persons, the client can send the following request:
    GET http://localhost/person/unique_identifier

This request asks for a person with a unique identifier. Another example is:
    DELETE http://localhost/person/unique_identifier

In this case, the client asks to delete the person with this unique identifier.
'''

#Step 3. Tasks
'''
You are asked to implement both of these endpoints in this exercise. 
You will also implement a count method that returns the total number of persons in the data list.
This will help confirm that the two methods GET and DELETE work, as required.
'''

#Step 3. Task 1: Create GET /count endpoint
'''
Create /count endpoint.

Add the @app.get() decorator for the /count URL.
Define the count function that simply returns the number of items in the data list.
'''
@app.route("/count")
def count():
    try:
        # Attempt to return a JSON response with the count of items in 'data'
        # Replace {insert code to find length of data} with len(data) to get the length of the 'data' collection
        return {"data count": len(data)}, 200
    except NameError:
        # If 'data' is not defined and raises a NameError
        # Return a JSON response with a message and a 500 Internal Server Error status code
        return {"message": "data not defined"}, 500

'''
Test the count method by calling the endpoint.
    curl -X GET -i -w '\n' "localhost:5000/count"

You should see an ouput with the number of items in the data list.
    HTTP/1.1 200 OK
    Server: Werkzeug/2.2.2 Python/3.7.16
    Date: Sat, 31 Dec 2022 22:41:35 GMT
    Content-Type: application/json
    Content-Length: 22
    Connection: close
    {
    "data count": 5
    }
'''


#Step 3. Taks 2.

'''
Task 2: Create GET /person/id endpoint
Implement the GET endpoint to ask for a person by id.
Create a new endpoint for http://localhost/person/unique_identifier.
The method should be named find_by_uuid.
It should take an argument of type UUID and return the person JSON if found.
If the person is not found, the method should return a 404 with a message of person not found.
Finally, the client (curl) should only be able to call this method by passing a valid UUID type id.
'''

@app.route("/person/<var_name>")
def find_by_uuid(var_name):
    # Iterate through the 'data' list to search for a person with a matching ID
    for person in data:
        # Check if the 'id' field of the person matches the 'var_name' parameter
        if person["id"] == str(var_name):
            # Return the person as a JSON response if a match is found
            return person
    # Return a JSON response with a message and a 404 Not Found status code if no matching person is found
    return {"message": "Person not found"}, 404

'''
Test the /person/uuid URL by calling the endpoint.
    curl -X GET -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53287

    You should see an ouput with the person and HTTP code of 200.
    HTTP/1.1 200 OK
    Server: Werkzeug/2.2.2 Python/3.7.16
    Date: Sat, 31 Dec 2022 22:48:32 GMT
    Content-Type: application/json
    Content-Length: 294
    Connection: close
    {
    "address": "637 Carey Pass",
    "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    "city": "Gainesville",
    "country": "United States",
    "first_name": "Lilla",
    "graduation_year": 1985,
    "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
    "last_name": "Aupol",
    "zip": "32627"
    }

If you pass in an invalid UUID, the server should return a 404 message.
    curl -X GET -i localhost:5000/person/not-a-valid-uuid

You should see an error in the output with a code of 404.
Flask automatically returns HTML, you will change the HTML in the next part
of the lab to return JSON by default on all errors, including 404.
#Alvaro: this part of the lab should be checked. We are aldreay handling the error (and showing a JSON), so no HTTP meassge will be sent.
#Alvaro: Unless we use: curl -X GET -i localhost:5000/this-route-does-note-exist
    HTTP/1.1 404 NOT FOUND
    Server: Werkzeug/2.2.2 Python/3.7.16
    Date: Sat, 31 Dec 2022 22:50:52 GMT
    Content-Type: text/html; charset=utf-8
    Content-Length: 207
    Connection: close
    <!doctype html>
    <html lang=en>
    <title>404 Not Found</title>
    <h1>Not Found</h1>
    <p>The requested URL was not found on the server. If you entered the URL manually, please check your spelling and try again.</p>


Finally, pass in a valid UUID that does not exist in the data list.
 The method should return a 404 with a message of person not found.
    curl -X GET -i localhost:5000/person/11111111-589a-43b6-9a5d-d1601cf51111

You should see a JSON response with an HTTP code of 404 and a message of person not found.
    HTTP/1.1 404 NOT FOUND
    Server: Werkzeug/2.2.2 Python/3.7.16
    Date: Sat, 31 Dec 2022 22:52:24 GMT
    Content-Type: application/json
    Content-Length: 36
    Connection: close
    {
    "message": "person not found"
    }
'''

#Task 3: Create DELETE /person/id endpoint
'''
Implement the DELETE endpoint to delete a person resource.

Create a new endpoint for DELETE http://localhost/person/unique_identifier.
The method should be named delete_by_uuid.
It should take in an argument of type UUID and delete the person from the data list with that id.
If the person is not found, the method should return a 404 with a message of person not found. 
Finally, the client (curl) should call this method by passing a valid UUID type id.
'''

#Alvaro: We could also use <id> instead of <uuid:id>, but then we are only compairing strings and Flask will not validate it is a 
#valid uuid, with <uuid:id> we cast id to uuiid. If Flask checks it and it is not a valid uuiid then Flask will return a 404
#without even calling the functino
@app.route("/person/<uuid:id>", methods=['DELETE'])
def delete_person(id):
    for person in data:
        if person["id"] == str(id):
            # Remove the person from the data list
            data.remove(person)
            # Return a JSON response with a message and HTTP status code 200 (OK)
            return {"message": "Person with ID deleted"}, 200
    # If no person with the given ID is found, return a JSON response with a message and HTTP status code 404 (Not Found)
    return {"message": "Person not found"}, 404

'''
Test the DELETE /person/uuid URL by calling the endpoint.
    curl -X DELETE -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53287

You should see an ouput with the id of the person deleted and a status code of 200.
    HTTP/1.1 200 OK
    Server: Werkzeug/2.2.2 Python/3.7.16
    Date: Sat, 31 Dec 2022 23:00:17 GMT
    Content-Type: application/json
    Content-Length: 56
    Connection: close
    {
    "message": "Person with ID 66c09925-589a-43b6-9a5d-d1601cf53287 deleted"
    }

You can now use the count endpoint you added earlier to test if the number of persons has reduced by one.
    curl -X GET -i localhost:5000/count

You should see the count returned reduced by one.
    HTTP/1.1 200 OK
    Server: Werkzeug/2.2.2 Python/3.7.16
    Date: Sat, 31 Dec 2022 23:06:55 GMT
    Content-Type: application/json
    Content-Length: 22
    Connection: close
    {
    "data count": 4
    }

If you pass an invalid UUID, the server should return a 404 message.
    curl -X DELETE -i localhost:5000/person/not-a-valid-uuid

You should see an error in the output with a code of 404. 
Flask automatically returns HTML, and we will change the HTML in the next
 part of the lab to return JSON by default on all errors, including 404.
    HTTP/1.1 404 NOT FOUND
    Server: Werkzeug/2.2.2 Python/3.7.16
    Date: Sat, 31 Dec 2022 23:05:09 GMT
    Content-Type: text/html; charset=utf-8
    Content-Length: 207
    Connection: close
    <!doctype html>
    <html lang=en>
    <title>404 Not Found</title>
    <h1>Not Found</h1>
    <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>

Finally, pass in a valid UUID that does not exist in the data list. The method should return a 404 with a message of person not found.
    curl -X DELETE -i localhost:5000/person/11111111-589a-43b6-9a5d-d1601cf51111

You should see a JSON response with an HTTP code of 404 and a message of person not found.
    HTTP/1.1 404 NOT FOUND
    Server: Werkzeug/2.2.2 Python/3.7.16
    Date: Sat, 31 Dec 2022 23:05:43 GMT
    Content-Type: application/json
    Content-Length: 36
    Connection: close
    {
    "message": "person not found"
    }
'''
