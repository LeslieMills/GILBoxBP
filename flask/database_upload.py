import os
from pymongo import MongoClient
import gridfs
from shutil import copy, rmtree

def dbInsertFile(filename, upload_directory):
    client = MongoClient(host="mongo",port=27017,username='root',password='pass',authSource='admin')
    # client = MongoClient()
    db = client[upload_directory]
    fs = gridfs.GridFS(db)
    init_path = "users"
    filepath = os.path.join(init_path,upload_directory,filename)
    fileID = fs.put(open(filepath, 'rb'))
    return fileID

def delete_file(fileID,upload_directory):
    client = MongoClient(host="mongo",port=27017,username='root',password='pass',authSource='admin')
    # client = MongoClient()
    db = client[upload_directory]
    fs = gridfs.GridFS(db)
    fs.delete(fileID)

def delete_database(upload_directory):
    client = MongoClient(host="mongo",port=27017,username='root',password='pass',authSource='admin')
    # client = MongoClient()
    client.drop_database(upload_directory)

def create_demo_file(filename, upload_directory):
    init_path = "users"
    dirpath = os.path.join(init_path,upload_directory)
    os.makedirs(dirpath, exist_ok=True)
    copy(filename, dirpath)

def delete_working_files(user_directory):
    dirpath = os.path.join("users",user_directory)
    rmtree(dirpath,ignore_errors=True)