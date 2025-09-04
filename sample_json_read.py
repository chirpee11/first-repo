
import json

def load_data(json_file_path):
    """Load JSON data from file."""
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(f"Successfully loaded rotor balance data from {json_file_path}")
        return data

    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.")
        raise
    except JSONDecodeError as e:
        print(f"Error: Invalid JSON in file '{json_file_path}': {e}")
        raise


json_data = load_data('rotor_balance_data.json')
print(json_data['sensorsplanesconditions'])
print(json_data['sensordata'])
print(json_data['weightplanedata'])
print(json_data['speedsconditionsweighting'])

