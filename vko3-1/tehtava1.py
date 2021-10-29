import requests
from google.cloud import storage
import time


sr = requests.get('https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json')
data = sr.json()

with open("checkpoint.txt", "w") as tiedosto:

    for d in data['items']:
        tiedosto.write(f'{d["parameter"]}\n')



def create_bucket(bucket_name):

    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)
    print("Bucket {} created.".format(bucket.name))




def upload_blob(bucket_name, source_file_name, destination_blob_name):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )


def main():
    bname = "jp-checkpoint-bucket"
    sourcefile = "C:/Users/JP/YourProjects/viikko3/checkpoint3/vko3-1/checkpoint.txt"
    blobname = "checkpoint"
    create_bucket(bname)
    time.sleep(60)
    upload_blob(bname, sourcefile, blobname)


if __name__=="__main__":
    main()