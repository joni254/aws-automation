import boto3

instance_id = 'i-014fce1bedfdc867a'
instance = ec2.instance(instance_id)
response = instance.terminate()
print(response)