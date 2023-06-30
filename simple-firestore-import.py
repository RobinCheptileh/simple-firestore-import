#!/usr/bin/env python3

import os
import sys
import json
import yaml

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def import_data(service_account_key_path, data_file, collection_name):
    try:
        cred = credentials.Certificate(service_account_key_path)
        firebase_admin.initialize_app(cred)

        db = firestore.client()

        data = get_data(data_file)
        check_data(data)

        doc_ref = db.collection(collection_name)
        for datum in data:
            if datum.get("id") or datum.get("_id"):
                doc_ref.document(datum.get("id")).set(datum)
            else:
                doc_ref.add(datum)
            print("Added: {}".format(datum))

    except Exception as error:
        print("\nERROR: {}".format(str(error)))
    else:
        print("\nImport complete")


def check_data(data):
    if isinstance(data, (list, tuple,)):
        for datum in data:
            if not isinstance(datum, (dict,)):
                raise ValueError("An object expected, got {}".format(type(datum)))
    else:
        raise ValueError("An array expected, got {}".format(type(data)))


def get_data(data_file):
    allowed_file_extensions = [".json", ".yaml", ".yml"]
    filename, file_extension = os.path.splitext(data_file)
    file_extension = file_extension.lower()

    if file_extension in allowed_file_extensions:
        if file_extension == ".json":
            return get_json_data(data_file)
        elif file_extension == ".yaml" or file_extension == ".yml":
            return get_yaml_data(data_file)

    raise ValueError("Invalid file type. Allowed file types include {}".format(allowed_file_extensions))


def get_json_data(data_file):
    with open(data_file, "r") as read_file:
        return json.load(read_file)


def get_yaml_data(data_file):
    with open(data_file, "r") as read_file:
        return yaml.load(read_file, Loader=yaml.FullLoader)


if __name__ == "__main__":
    try:
        if len(sys.argv) == 4:
            service_account_path = sys.argv[1]
            data_file_path = sys.argv[2]
            name_of_collection = sys.argv[3]
        else:
            service_account_path = input("Path to serviceAccountKey.json: ")
            data_file_path = input("Path to data file: ")
            name_of_collection = input("Name of collection: ")

        import_data(service_account_path, data_file_path, name_of_collection)
    except KeyboardInterrupt as keyboard_error:
        print("\nProcess interrupted")
    finally:
        print("\nGood Bye!")
