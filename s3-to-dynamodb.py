import boto3

rekognition = boto3.client('rekognition')
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    bucket = event["Records"][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    # key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    try:
        # response = s3.get_object(Bucket=bucket, Key=key)
        
        response = rekognition.detect_text(
            Image={
                # 'Bytes': b'bytes',
                'S3Object': {
                    'Bucket': bucket,
                    'Name': key
                }
            }
        )
        
        # text = response["Body"].read().decode()
        # data = json.loads(text)
        
        # print(data)
        print(bucket)
        print(key)
        
        plat_nomor = response['TextDetections']['DetectedText']
        print(plat_nomor)
        
        
        dynamodb.put_item(
            TableName='cobafinal',
            Item={
                'namaGambar':{'S':key},
                'plat':{'S':plat_nomor}
            }
        )
        
        
        
        # for record in transactions:
        #    print(record['transType'])
        return 'Success!'
        
    except Exception as e:
        print(e)
        raise e