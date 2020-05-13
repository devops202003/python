import boto3
import json
from botocore.exceptions import ClientError

f = open('envData',)
data = json.load(f)

ec2 = boto3.resource('ec2')

try:
  instances = ec2.create_instances(
     ImageId=data[0]['dev']['ami'],
     InstanceType=data[0]['dev']['instance_type'],
     KeyName=data[0]['dev']['keypair'],
     MinCount=1,
     MaxCount=1
  )
  print(instances)
except ClientError:
  print("Not able to create instance" + str(e) )
else:
  print("Success")
f.close()
