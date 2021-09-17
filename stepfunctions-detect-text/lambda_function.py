import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('rekognition')
    
    S3Bucket = event['S3Bucket']
    Key = event['Key']

    response = client.detect_text(Image={'S3Object':{'Bucket':S3Bucket,'Name':Key}})

    results = response.get('TextDetections')

    
    texts = [i.get('DetectedText') for i in results]
    
    return { 'texts': texts }
