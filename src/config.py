import json


def load_config(config_path='../config.json'):
    with open(config_path, 'r') as config_file:
        config_data = json.load(config_file)
    return config_data


if __name__ == "__main__":
    config = load_config()
    print(config['HCP_DIR'])
