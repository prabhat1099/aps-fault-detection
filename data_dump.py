import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolab")

DATABASE_NAME='aps'
COLLECTION_NAME="sensor"

DATA_PATH="/config/workspace/aps_failure_training_set1.csv"

if __name__=="__main__":
    # To read csv file
    df=pd.read_csv(DATA_PATH)
    print(f"Rows and columns are: {df.shape}")

    # To convert dataframe into json file to dump into Mongodb
    df.reset_index(drop=True,inplace=True)
    json_record=list(json.loads(df.T.to_json()).values())
    #print(json_record[0])
    
    # To insert converted json record to mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    print('Successfully inserted all data')