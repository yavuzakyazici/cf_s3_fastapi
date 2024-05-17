from fastapi import FastAPI, UploadFile
import os
from dotenv import load_dotenv
import boto3
from botocore.exceptions import ClientError

"""
All of these params below should be in a .env file loaded with load_dotenv()

load_dotenv()

R2_BUCKET_NAME = os.getenv("R2_BUCKET_NAME")
ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
SECRET_ACCESS_KEY_ID = os.getenv("SECRET_ACCESS_KEY_ID")
ENDPOINT_URL_DEFAULT = os.getenv("ENDPOINT_URL_DEFAULT")
REGION_NAME = os.getenv("REGION_NAME")
"""

"""
These are dummy place holder params
You should get real params from CloudFlare R2 after creating your bucket
and your API Key at CloudFlare Dashboard
This example obivously will NOT work before creating your bucket and getting API key
"""
R2_BUCKET_NAME = "My_Bucket_Name"
ACCESS_KEY_ID = "My_Access_Key_Id"
SECRET_ACCESS_KEY_ID = "My_Secret_Access_Key_Id"
ENDPOINT_URL_DEFAULT = "My_Endpoint_Url_Default"
REGION_NAME = "auto"


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to CloudFlare R2 Boto3 example"}


"""
create your boto3 client
"""
s3 = boto3.client(
    service_name ="s3",
    endpoint_url = ENDPOINT_URL_DEFAULT,
    aws_access_key_id = ACCESS_KEY_ID,
    aws_secret_access_key = SECRET_ACCESS_KEY_ID,
    region_name=REGION_NAME, # Must be one of: wnam, enam, weur, eeur, apac, auto
)

"""
you can get your file info before downloading
"""
@app.get("/get_file_info/{folder_name}/{file_name}")
async def get_file_info(folder_name:str, file_name:str):
    try:
        if folder_name is not None:
            # this is a wrokaround since FastAPI does not accept / characters
            # or rather sees it as @app.get request path and returns 404
            # if you have deeper folder structure either use different buckets or modify this code
            folder_name = f"{folder_name}/"
        object_information = s3.head_object(Bucket=R2_BUCKET_NAME, Key=f"{folder_name}{file_name}")
        return object_information
    except ClientError as error:
        raise error


@app.get("/download/{file_name}")
async def download(file_name:str):
    try:
        s3.download_file(Bucket=R2_BUCKET_NAME, Key=f"{file_name}", Filename=f"{file_name}" )
        object_information = s3.head_object(Bucket=R2_BUCKET_NAME, Key=f"{file_name}")
        return object_information
    except ClientError as error:
        raise error


@app.post("/upload/")
def create_upload_file(file: UploadFile):
    try:
        f_name = file.filename
        s3.upload_fileobj(file.file, R2_BUCKET_NAME, f_name)
        object_information = s3.head_object(Bucket=R2_BUCKET_NAME, Key=f"{f_name}")
        return object_information
    except ClientError as error:
        raise error