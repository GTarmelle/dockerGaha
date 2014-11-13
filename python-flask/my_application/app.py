from flask import Flask
from flask import request
import os
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

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
@app.route('/euler1')
def euler_E1():
    result = ""
    sum = 0
    for i in range(1000):
      if((i%3 == 0) or (i%5 == 0)):
        sum += i
    result += str(sum) + "\n" 
    return result

@app.route('/euler2')
def euler_E2():
  limit = 4000000
  result = ""
  sumeven = 2
  swap = 0
  fprev =1
  factu = 2
  while (factu <= limit):
    swap = factu
    factu = fprev + factu
    fprev = swap
    if(factu%2 == 0):
      sumeven += factu
  result += str(sumeven) + "\n" 
  return result


@app.route('/listqueues')
def queues():
  result = ""
  # This script created a queue
  #
  # Author - Paul Doyle Aug 2013
  # modified by Gaha to list all queues in us-east-1 and eu-west-1
  #


  conn = boto.sqs.connect_to_region("us-east-1", aws_access_key_id='GKIAIR7EH3TNSTDUCWKH', aws_secret_access_key='P2FZT5mrLYy8gX7kS1q0p4ObQYXTwGnaiUm+rxHE')

#  rs = conn.get_all_queues()
#  for q in rs:
#          result += q.id + "\n"

  #irland is in eu-west-1 region
#  myconn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id='GKIAIR7EH3TNSTDUCWKH', aws_secret_access_key='P2FZT5mrLYy8gX7kS1q0p4ObQYXTwGnaiUm+rxHE')

#  rs = myconn.get_all_queues()
#  for q in rs:
#          result += q.id + "\n"

  return result

@app.route('/post/<int:post_id>')
def show_post(post_id):
#show the post with the giving int id
   return 'post %d' %post_id

@app.route('/projects/')
def project():
   return "the project page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
