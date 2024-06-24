from azure.storage.blob import BlobServiceClient
import os


#change cridentials detils with your's details 
storage_account_key = "sXZHmfAtgr3V3JAEgkTYO9TwHXWS8ZNt8QrQm*********************************************"
storage_account_name = "namra2511"
connection_string = "DefaultEndpointsProtocol=https;AccountName=namra2511;AccountKey=sXZH***************************************************************************************"
container_name = "namra"

def uploadToBlobStorage(file_path, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client =blob_service_client.get_blob_client(container=container_name,blob=file_name)

    with open(file_path,"rb") as data:
        blob_client.upload_blob(data)
        print("Upload "+file_name+" file")

uploadToBlobStorage('C:\\Users\\namra\\OneDrive\\Documents\\cloud\\task.png','cloud')