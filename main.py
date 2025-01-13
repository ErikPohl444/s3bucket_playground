import boto3
import json

AWS_BUCKET_EAP = 'first-aws-bucket-1eap'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("env.json") as fhandle:
        cfg = json.load(fhandle)
    pub, priv = cfg["public"], cfg["private"]
    session = boto3.Session(aws_access_key_id=pub,
                            aws_secret_access_key=priv
                            )
    s3_resource = session.resource('s3')
    # s3_resource.create_bucket(Bucket="first-aws-bucket-1eap")
    for bucket in s3_resource.buckets.all():
        print(bucket.name)

    # s3_resource.Object(AWS_BUCKET_EAP, 'KilroySchematic.svg'). \
    #     upload_file(Filename='C:\\Users\\epohl\\projects\\s3bucket_playground\\KilroySchematic.svg')

    # s3_resource.Object(AWS_BUCKET_EAP, 'KilroySchematic.svg').download_file(
    #     'C:\\Users\\epohl\\projects\\s3bucket_playground\\KWH.svg')

    # s3_resource.Object(
    #     AWS_BUCKET_EAP,
    #     'KilroySchematic2.svg').copy_from(
    #     CopySource="first-aws-bucket-1eap/KilroySchematic.svg"
    # )

    s3_resource.Object(AWS_BUCKET_EAP, 'KilroySchematic2.svg').delete()

    pythonusecase = s3_resource.Bucket(name=AWS_BUCKET_EAP)
    for object in pythonusecase.objects.all():
        print(object.key)

    try:
        bucket = s3_resource.Bucket(AWS_BUCKET_EAP)
        # bucket.objects.all().delete()
        s3_resource.Bucket(AWS_BUCKET_EAP).delete()
    except Exception as e:
        print(e)
