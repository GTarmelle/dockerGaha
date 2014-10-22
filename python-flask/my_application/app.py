from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
@app.route('/post/<int:post_id>')
def show_post(post_id):
#show the post with the giving int id
   return 'post %d' %post_id

@app.route('/projects/')
def project():
   return "the project page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
