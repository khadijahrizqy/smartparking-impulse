# **Recognition in Parking Gate**

## **What is it?**
Recognition in Parking Gate or RIPE is an Artificial Intelligence solution for a modern and effective parking barrier gate system where vehicles will be automatically scanned for their point of entry and exit with Image Recognition technology.<br>

## **AWS Features that we used**
1. S3 Bucket
2. DynamoDB
3. Lambda Function
4. Rekognition
  
## **How it works**
Photo uploaded from website endpoint to S3 Bucket. S3 triggers Lambda Function to query POST to DynamoDB. Upon uploading license number photo to DynamoDB, it will trigger Lambda function to use text Rekognition to determine the plates. The face image and license number will be in DynamoDB for safe-keeping. Upon exit, the same function will happen. If the license number exists in DynamoDB, it will trigger Lambda Function to compare the face images upon entry and exit. If Rekognition deems it a match, the gate will open.

## **Further Developments**
We will develop the Rekognition part to compare the two photos.

<br><br>
