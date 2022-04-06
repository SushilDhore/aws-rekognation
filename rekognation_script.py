import cv2

cap = cv2.VideoCapture(0)
myimage = "pranay.jpg"
ret , photo = cap.read()
cv2.imwrite( myimage , photo)
cap.release()

region = 'ap-south-1'
bucket = 'mybucket5432'


import csv
import boto3


upimage = "file.jpg"

with open('credentials.csv.txt', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3] 

s3 = boto3.resource('s3')
s3.Bucket(bucket).upload_file(myimage , "file.jpg")

rek = boto3.client('rekognition' , region )

response = rek.detect_labels(
    Image={
          'S3Object': {
              'Bucket': bucket,
              'Name': upimage,
          }
      },
      MaxLabels=10,
      MinConfidence=90
  ) 

for i in range(5):
      print ( response['Labels'][i]['Name'] )