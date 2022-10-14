from sys import path
import os
path.append('src')  #go to src directory to import
from flask import Flask, render_template, redirect
from CASClient import CASClient
import secrets
import validation

# app info
app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


@app.route('/')
def hello():
    return render_template('initial.html')

@app.route('/application')
def application():
    print(os.getenv('DB_URL'))
    netid = str(CASClient().Authenticate())
    print(netid)
    is_in_club = validation.get_club_status(netid, 1)
    print(is_in_club)
    return render_template('inside.html', CASValue = netid, validation = is_in_club)

if __name__ == '__main__':
    app.run(host='localhost', port=5555)
