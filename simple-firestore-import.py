#!/usr/bin/env python3

import os
import sys
import json
import yaml

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def import_data(service_account_key_path, data_file, collection_name):
    allowed_file_extensions = ["json", "yaml", "yml"]

    try:
        cred = credentials.Certificate(service_account_key_path)
        firebase_admin.initialize_app(cred)

        db = firestore.client()

        filename, file_extension = os.path.splitext(data_file)

        if file_extension.lower in allowed_file_extensions:
            pass
        else:
            raise ValueError("Invalid file type. Allowed file types include {}".format(allowed_file_extensions))

    except Exception as error:
        print(str(error))


if __name__ == "__main__":
    if len(sys.argv) == 4:
        service_account_path = sys.argv[1]
        data_file_path = sys.argv[2]
        collection_name = sys.argv[3]
    else:
        service_account_path = input("Path to serviceAccountKey.json: ")
        data_file_path = input("Path to data file: ")
        collection_name = input("Name of collection: ")

    import_data(service_account_path, data_file_path, collection_name)
