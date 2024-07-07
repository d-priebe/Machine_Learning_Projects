# from database import Mongo_DB
from .database import Mongo_DB

import argparse


def main(args):
    import sys
    print(sys.path)

    # Instantiate DB 
    database = Mongo_DB(args.database, args.collections, args.local_dir)
    # Run upload process
    database.upload_csvs()
    print("All CSV files have been uploaded to MongoDB.")



def cli_main():
    import sys
    parser = argparse.ArgumentParser(description="Run Upload process")
    parser.add_argument("-d", "--database", type=str, required = True, help= "Loads memory value of key for a given scraping objective", default="recruit-data-cluster")
    parser.add_argument("-c", "--collections", type=str, required = True, help= "Loads memory value of key for a given scraping objective", default="Team_Recruiting")
    parser.add_argument("-l", "--local_dir", type=str, required=True,help = "Loads Team ID Value data for URL Scraping", default= "data/")
    print("CLI Arguments: ", sys.argv[1:])  # This will print the arguments passed to the script
    args = parser.parse_args()
    main(args)

if __name__ == "__main__":
    cli_main()