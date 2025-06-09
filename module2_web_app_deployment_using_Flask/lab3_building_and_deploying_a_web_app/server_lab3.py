from flask import Flask, render_template, request
app = Flask(__name__)

#Create the routes
'''Create the Home Route
Define a route for the home page (“/“) using the @app.route decorator.
Inside the route function, return a response
by rendering a template called “home.html”
and passing a variable name with the value ‘John’.
Use the render_template function from Flask.
'''
@app.route('/')
def home():
    name = 'John'
    return render_template('home.html', name=name)

'''Create an HTML file called “home.html” in your templates directory.
    mkdir templates
    cd templates
    touch home.html
'''

'''Use the appropriate HTML tags to structure the page.
Display a heading that says “Welcome to the Home Page!”
Use the {{ name }} variable to display the value passed from the route function.

    <!DOCTYPE html>
    <html>
    <head>
        <title>My Flask App</title>
        <style>
            html, body {
                height: 100%;
                margin: 0;
                padding: 0;
            }
            body {
                display: flex;
                flex-direction: column;
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
            }
            header {
                background-color: #333333;
                padding: 20px;
                color: #ffffff;
                text-align: center;
            }
            main {
                flex: 1;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            footer {
                background-color: #333333;
                padding: 10px;
                color: #ffffff;
                text-align: center;
                font-size: 12px;
            }
            h1 {
                color: #333333;
                text-align: center;
                margin-top: 50px;
            }
            p {
                color: #666666;
                text-align: center;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>My Flask App</h1>
        </header>
        <main>
            <h1>Hello, {{ name }}!</h1>
            <p>Welcome to my Flask app.</p>
        </main>
        <footer>
            &copy; 2023 My Flask App. All rights reserved.
        </footer>
    </body>
    </html>

Create the About Route
Define a route for the about page (“/about”) using the @app.route decorator.
Inside the route function, return a string response that represents an HTML page.
You can use a multi-line string or create a separate HTML file and return its contents.
'''
@app.route('/about')
def about():
    return render_template('about.html')

'''
Create an HTML file called “about.html” in your templates directory.
    touch about.html

Use the appropriate HTML tags to structure the page.
Add content in the about page saying “This is the about page.”
Style the content of the page using the style tag.

<DOCTYPE! html>
    <html>
            <head>
                <title>About</title>
                <style>
                    .about-page {
                        font-family: Arial, sans-serif;
                        font-size: 18px;
                        color: #333333;
                        text-align: center;
                        padding: 50px;
                        background-color: #f2f2f2;
                    }
                </style>
            </head>
            <body>
                <div class="about-page">
                    This is the about page.
                </div>
            </body>
        </html>


Create the Contact Route
Define a route for the contact page (“/contact”) using the @app.route decorator.
Inside the route function, return a response by rendering a template called “contact.html” using the render_template function.
Double-check that your work matches the solution below.
'''
@app.route('/contact')
def contact():
    return render_template('contact.html')

'''
Create an HTML file called “contact.html” in your templates directory.
    touch contact.html

Use the appropriate HTML tags to structure the page.
Add a contact form with fields for name, email, and message.
Include a submit button for the form.

<!DOCTYPE html>
<html>
<head>
    <title>My Flask App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
        }
        h1 {
            color: #333333;
            text-align: center;
            margin-top: 50px;
        }
        p {
            color: #666666;
            text-align: center;
            margin-top: 20px;
        }
        form {
            max-width: 400px;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 5px;
        }
        input[type="text"],
        textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #cccccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        input[type="submit"] {
            background-color: #4caf50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Hello!</h1>
    <p>Contact Us.</p>
    <form>
        <input type="text" placeholder="Name" name="name">
        <input type="text" placeholder="Email" name="email">
        <textarea placeholder="Message" name="message"></textarea>
        <input type="submit" value="Submit">
    </form>
</body>
</html>

Create the User Profile Route
Define a route with a dynamic parameter for the username (“/users/<username>“) using the @app.route decorator.
Inside the route function, retrieve the dynamic parameter using a parameter in the function definition (e.g., def user_profile(username):).
Return a response by rendering a template called “profile.html” and pass the username variable to the template.
'''
@app.route('/users/<username>')
def user_profile(username):
    return render_template('profile.html', username=username)

'''
Create an HTML file called “profile.html” in your templates directory.
    touch profile.html

Use the appropriate HTML tags to structure the page.
Display a heading that says “User Profile: {{ username }}”
Include additional information or sections as desired to showcase the user’s profile.
<!DOCTYPE html>
<html>
<head>
    <title>User Profile</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            color: #333333;
            text-align: center;
            margin-top: 50px;
        }
        h2 {
            color: #666666;
            text-align: center;
            margin-top: 20px;
        }
        p {
            color: #999999;
            text-align: center;
            margin-top: 20px;
        }
        .profile-image {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin: 0 auto;
            display: block;
            background-color: #cccccc;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>User Profile</h1>
        <h2>Welcome, {{ username }}!</h2>
        <p>This is the profile page for user {{ username }}.</p>
        <img class="profile-image" src="https://images.pexels.com/photos/39866/entrepreneur-startup-start-up-man-39866.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="Profile Image">
    </div>
</body>
</html>
'''

#Add the necessary code to run the Flask server.
'''Use the if __name__ == '__main__': condition to ensure that the server is only run
when the script is executed directly (not imported as a module).
Inside the condition, call the run() method on the Flask application (app).
'''
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 

'''
Open a terminal or command prompt and navigate to the directory where your server.py file is located.
Run the Flask server by executing the following command:
    python3.11 server.py

Then, navigate to the Skills Network Toolbox and click on the Launch Application.
Then, write the PORT number and then click on the Launch Application icon as shown in the screenshot below.

You should then see this output: 
Alvaro# see lab of the website for the image (output)
'''
