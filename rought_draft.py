# !/usr/bin/env python

'''
    File name: rough_draft.py
    Author: Su-Young Hong
    Date created: 09/01/2016
    Date last modified: 09/01/2016
    Python Version: 2.7
'''
# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for

from resources import *

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html', companies = [])



# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is
# accepting: POST requests in this case
@app.route('/addInfo/', methods=['POST'])
def addInfo():
    company=request.form['Company']
    info=request.form['Information']
    records = read_json()
    updateInfo(records, company, info)
    write_json(records)
    companies, fields = getFields(records)
    return render_template('form_submit_part2.html', companies = companies, fields = fields)



# Run the app :)
if __name__ == '__main__':
  app.run(
        #host="0.0.0.0",
        #port=int("80")
  )
