import json
import re
import argparse
import sys

def ends_with_list_index(s):
    pattern = re.compile(r'\[\d+\]$')
    return bool(pattern.search(s))

def split_index(s):
    pattern = re.compile(r'^(.*?)(?:\[(\d+)\])?$')
    match = pattern.match(s)
    return match.groups()

def ungron(data):
    result = {}
    for line in data.split('\n'):
        line = line[:-1] # Remove semicolon
        parts = line.split('=')
        if len(parts) == 2:
            key, value = parts
            key = key.strip()
            value = value.strip()

            keys = key.split('.')
            current = result
            
            for k in keys[:-1]:
                if ends_with_list_index(k):
                    s, idx = split_index(k)
                    current = current[s][int(idx)]
                else:
                    current = current[k]

            if ends_with_list_index(keys[-1]):
                s, idx = split_index(keys[-1])
                current[s].append(json.loads(value))
            else:
                current[keys[-1]] = json.loads(value)

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ungron does the opposite of gron.")
    parser.add_argument("filename", nargs='?', help="Name of the text file to undo.")
    args = parser.parse_args()
    if args.filename:
        with open(args.filename, 'r') as file:
            gron_data = file.read()
            original_json = ungron(gron_data)
    else:
        text = sys.stdin.read()
        original_json = ungron(text)

# Print the reconstructed JSON
    print(json.dumps(original_json, indent=2))
    sys.exit(0)
