import csv
import json

from config.config_data import accesstoken


def write_to_csv(testdata,csvfile):
    f = open(csvfile,mode='w',encoding='utf8',newline='')
    csvfile = csv.writer(f)
    for data in testdata:
        tmp = []
        tmp.append(json.dumps(data[0]))
        tmp.append(data[1])
        tmp.append(json.dumps(data[2]))
        csvfile.writerow(tmp)

def read_csv_to_dict(csvfile):
    f = open(csvfile,mode='r',encoding='utf8')
    csvfile = csv.reader(f)

    data =[]
    for line in csvfile:
        tmp = []
        tmp.append(json.loads(line[0]))
        tmp.append(int(line[1]))
        tmp.append(json.loads(line[2]))
        data.append(tuple(tmp))

    return data

if __name__ == '__main__':
    test_ddt_data = [
        ({'accesstoken': '', 'title': 'hellords', 'tab': 'ask', 'content': 'cccccccccc'}, 401, '错误的accessToken'),
        ({'accesstoken': accesstoken, 'title': '', 'tab': 'ask', 'content': 'cccccccccc'}, 400, '标题不能为空'),
        ({'accesstoken': accesstoken, 'title': 'sfdsdf', 'tab': '', 'content': 'cccccccccc'}, 400, '必须选择一个版块'),
        ({'accesstoken': accesstoken, 'title': 'asdfdsf', 'tab': 'ask', 'content': ''}, 400, '内容不可为空')
    ]
    write_to_csv(testdata=test_ddt_data,csvfile='data.csv')
    data = read_csv_to_dict(csvfile='data.csv')
    print(data)