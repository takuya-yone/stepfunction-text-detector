import json
import boto3
from datetime import date, datetime


BucketName = 'xxxxxxxxx'

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


def lambda_handler(event, context):
    
    client = boto3.client('s3')
    response = client.list_objects_v2(Bucket=BucketName, Prefix='text_detection/')
    objects = response['Contents']
    del objects[0]
    # print(type(objects))    
    # print(objects[0].keys())

    # object_keys = [i['Key'] for i in objects]
    
    payload = []
    
    for object in objects:
        payload.append({'S3Bucket':BucketName,'Key':object['Key']})

    return {'imageList':payload}