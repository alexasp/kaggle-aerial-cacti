# -*- coding: utf-8 -*-
"""
Created on Fri May 10 14:41:12 2019

@author: alexa
"""

import sys
import json
import boto3

client = boto3.client('runtime.sagemaker')

image_file_path = sys.argv[1]
endpoint = 'aerial-cactus'

with open(image_file_path, 'rb') as f:
    payload = f.read()

response = client.invoke_endpoint(EndpointName=endpoint, ContentType='application/x-image', Body=payload)
result = json.loads(response['Body'].read().decode())

print('NotCactus,Cactus')
print(result)