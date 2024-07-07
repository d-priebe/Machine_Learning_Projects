
from pymongo import MongoClient
from pathlib import Path
import pandas as pd
# from utils.utility_funcs import open_file
from ..utils.utility_funcs import open_file



class Mongo_DB:
    def __init__(self, db_name, collection, csv_directory):
        self.csv_directory = Path.cwd() / 'Projects/data_gen'/csv_directory
        self.client = self.connect_to_mongo()
        self.db = self.client[db_name]
        self.collection = collection

    def connect_to_mongo(self):
        """Establishes a connection to the MongoDB database."""
        password = open_file(Path.cwd() / 'Projects/data_gen/authentication' / 'mongodb_pass.txt')
        connection_string = f"mongodb+srv://drewpriebe6:{password}@recruit-data-cluster.maprc3u.mongodb.net/"
        print("Database Connection Established.")
        return MongoClient(connection_string)

    def upload_csvs(self):
        """Uploads CSV files from the specified directory to MongoDB."""
        for file_path in self.csv_directory.glob('*.csv'):
            if 'recruiting' in file_path.stem.lower(): 
                self.process_file(file_path)

    def process_file(self, file_path):
        """Processes a single CSV file and uploads its contents to MongoDB."""
        data = pd.read_csv(file_path)
        data_dict = data.to_dict("records")
        collection = self.db[self.collection]
        collection.insert_many(data_dict)
        print(f"Inserted data from {file_path.name} into collection {self.collection}")

    def list_databases(self):
        """Lists all databases in MongoDB cluster."""
        return self.client.list_database_names()