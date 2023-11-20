import json
import argparse
import sys

def gron(data, parent_key):
    if isinstance(data, dict):
        print(f"{parent_key} = {{}};")
        for key, value in data.items():
            gron(value, f"{parent_key}.{key}" if parent_key else key)
    elif isinstance(data, list):
        print(f"{parent_key} = [];")
        for index, value in enumerate(data):
            gron(value, f"{parent_key}[{index}]")
    else:
        print(f"{parent_key} = {json.dumps(data)};")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="gron transforms JSON into discrete assignments.")
    parser.add_argument("filename", nargs='?', help="Name of the json file to transform")
    parser.add_argument("--obj", help="Specify base object")
    args = parser.parse_args()

    if args.obj:
        base_object = args.obj
    else:
        base_object = 'json'

    if args.filename:
        with open(args.filename, 'r') as file:
            json_data = json.load(file)
            gron(json_data, base_object)
    else:
        text = json.loads(sys.stdin.read())
        gron(text, base_object)