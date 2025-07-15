#Making your first server

from flask import Flask, render_template
from requests import *

app = Flask(__name__) #creating a flask instance

@app.route('/')
def hello_world():
    return "<h1 style='text-align:center'> Hello World! </h1>"
    '<p> This is a paragraph </p>'

@app.route('page/<int: number>')
def page(number):
    return f"This is page {number}"

@app.route('/')
def home():
    return render_template('index.html')
#create a folder 'template' add the html file to it
#create a folder static add the images/logos and the style.css file

#XSS WITH SERVER (reflected)
@app.route('/about_me', methods=['GET','POST'])
def about_me():
    user_input = ''
    if request.methods == 'POST':
        user_input = request.form.get('xss_input','')
    return render_template('about_me.html' user_input = user_input)

'''
<body>
    <h1> About me </h1>
    <p> This page is about me </p>
    <form method = 'post' action ='/about-me'>
        <input type = 'text' name = 'xss_input'>
        <input type ='submit' value='submit>
    </form>
-> to render info from server
    <div> {{ user_input | safe }} </div>
'''
 
if __name__ == "__main__":
    app.run(debu=True)