import json
import sys
import json


def transform_json_to_data(fileName):
    with open(fileName, 'r', encoding='utf-8') as file:
        data = json.load(file)
        print("succeess to transfrom %s to data!"%fileName)
        return data


def transform_data_to_json(fileName, data):
    with open(fileName, 'w') as file:
        json.dump(data, file, indent=4, sort_keys=True)
    print("success to wirte new data to %s"%fileName)

if __name__ == "__main__":
    acc = sys.argv[1]
    pwd = sys.argv[2]
    data = transform_json_to_data(fileName="account.json")
    new_append_dict = {}
    new_append_dict['account'] = acc
    new_append_dict['password'] = pwd
    data.append(new_append_dict)
    transform_data_to_json(data=data, fileName="account.json")
    print("now_data is as below!")
    print(data)
    
