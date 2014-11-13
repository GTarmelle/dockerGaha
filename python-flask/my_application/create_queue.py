import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id='AKIAIR7EH3TNSTDUCWKA', aws_secret_access_key='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')

#create a queue
q = conn.create_queue('D14123111_Gaha')

#write a message to the queue
m = Message()
m.set_body('create my first message')
q.write(m)

rs = conn.get_all_queues()
for x in rs:
  print(x)

