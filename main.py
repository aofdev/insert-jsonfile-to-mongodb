import os
import fire
import json
import dateutil.parser
from pymongo import MongoClient, errors
from typing import Dict


def datetime_parser(json_dict: Dict) -> Dict:
    for (key, value) in json_dict.items():
        try:
            json_dict[key] = dateutil.parser.parse(value)
        except (ValueError, AttributeError, TypeError):
            pass
    return json_dict


def insert(mongo_uri: str, mongo_db: str, mongo_collection: str, jsonfile: str) -> None:
    with open(jsonfile, "r") as file:
        raw_data_from_file = json.loads(file.read(), object_hook=datetime_parser)
        file.close()
        try:
            client = MongoClient(mongo_uri)
            db = client[mongo_db]
            collection = db[mongo_collection]
            collection.insert_one(raw_data_from_file)
            client.close()
            print("Insert Success ✅")
        except errors.DuplicateKeyError:
            print("Duplicate key ⚠️")
        except Exception as err:
            print(f"Error something went wrong {err}")


if __name__ == "__main__":
    fire.Fire(insert)
