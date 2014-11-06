import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

def queues():
  result = ""
  # This script created a queue
  #
  # Author - Paul Doyle Aug 2013
  # modified by Gaha to list all queues in us-east-1 and eu-west-1
  #


  conn = boto.sqs.connect_to_region("us-east-1", aws_access_key_id='AKIAJ2BJXBF74JPNZKCQ', aws_secret_access_key='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')

  rs = conn.get_all_queues()
  for q in rs:
          result += q.id + "\n"

  #irland is in eu-west-1 region
  myconn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id='AKIAJ2BJXBF74JPNZKCQ', aws_secret_access_key='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')

  rs = myconn.get_all_queues()
  for q in rs:
          result += q.id + "\n"

  return result
  
print(queues())