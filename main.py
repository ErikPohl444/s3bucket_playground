import boto3
import json


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("env.json") as fhandle:
        cfg = json.load(fhandle)
    pub, priv = cfg["public"], cfg["private"]
    session = boto3.Session(aws_access_key_id=pub,
                            aws_secret_access_key=priv
                            )
    s3_resource = session.resource('s3')
    s3_resource.create_bucket(Bucket="first-aws-bucket-1eap")
    for bucket in s3_resource.buckets.all():
        print(bucket.name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
