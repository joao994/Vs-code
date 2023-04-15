## get file from s3

import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)
    
data = s3.Object('meubucket994','my-file.txt').get()







    
        




