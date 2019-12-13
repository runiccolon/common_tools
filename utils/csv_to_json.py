import csv
import json


def csv_to_json(csv_path, json_path):
    """

    :param csv_path: 要打开的csv文件路径
    :param json_path: 要保存的json文件路径
    :return:
    """
    csvfile = open(csv_path, 'r', encoding='utf-8-sig')
    jsonfile = open(json_path, 'w', encoding='utf-8')

    fieldnames = tuple(csvfile.readline().split(','))
    print(type(fieldnames))
    print(fieldnames)

    reader = csv.DictReader(csvfile, fieldnames)
    print(reader)
    print(type(reader))

    out = json.dumps([row for row in reader], ensure_ascii=False)
    jsonfile.write(out)
    print(json.loads(out))

    return out


if __name__ == '__main__':
    csv_to_json(json_path='../data/广告主.json'
                , csv_path="../data/广告主.csv")
