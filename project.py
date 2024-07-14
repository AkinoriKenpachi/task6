import argparse
import json
import xmltodict
import yaml

def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert data between XML, JSON, and YAML formats.")
    parser.add_argument('input_file', help="Path to the input file")
    parser.add_argument('output_file', help="Path to the output file")
    return parser.parse_args()

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        return None

def write_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error writing JSON file: {e}")

def convert_data(input_file, output_file):
    input_ext = input_file.split('.')[-1]
    output_ext = output_file.split('.')[-1]

    if input_ext == 'json':
        data = read_json(input_file)
    elif input_ext == 'xml':
        with open(input_file, 'r') as file:
            data = xmltodict.parse(file.read())
    elif input_ext in ['yml', 'yaml']:
        with open(input_file, 'r') as file:
            data = yaml.safe_load(file)
    else:
        raise ValueError("Unsupported input file format")

    if output_ext == 'json':
        write_json(data, output_file)
    elif output_ext == 'xml':
        with open(output_file, 'w') as file:
            file.write(xmltodict.unparse(data, pretty=True))
    elif output_ext in ['yml', 'yaml']:
        with open(output_file, 'w') as file:
            yaml.dump(data, file)
    else:
        raise ValueError("Unsupported output file format")

if __name__ == "__main__":
    args = parse_arguments()
    convert_data(args.input_file, args.output_file)
