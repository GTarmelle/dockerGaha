from flask import Flask
from flask import request
import os
app = Flask(__name__)

@app.route("/")
def hello():
   #list all files
    return "Hello World!"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
@app.route('/files')
def show_files():
    path = "./uploads/"
    directories = os.listdir(path)
    allFiles = ""
    for file in directories:
    	allFiles += file + "\n" 
    return allFiles
@app.route('euler1')
def euler_E1():
    sum = 0
    for i in range(1000):
	if((i%3 ==0) or (i%5==0)):
	   sum += i
    return sum

@app.route('/post/<int:post_id>')
def show_post(post_id):
#show the post with the giving int id
   return 'post %d' %post_id

@app.route('/projects/')
def project():
   return "the project page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
