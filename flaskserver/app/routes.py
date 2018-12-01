from app import app
from flask import request, Flask
from flask_restful import Resource, Api


api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Fuad'}
    x = 20
    y = 20+x
    #y=str(y)
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
        <h2> ''' + str(y+y) + ''' </h2> 
    </body>
</html>'''