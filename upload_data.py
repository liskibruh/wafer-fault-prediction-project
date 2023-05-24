from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://oo_wais:Ahmed55555@cluster0.ioqcvgd.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"
# read data as a dataframe
df=pd.read_csv(r"C:\Users\oo_wa\OneDrive\Desktop\sensor-fault-detection\notebooks\wafer_23012020_041211.csv")
df = df.drop("Unnamed: 0", axis=1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
