import boto3

def getBedrockClient():
    return boto3.client('bedrock-runtime', region_name='us-east-1')

def getS3Client():
    return boto3.client('s3')