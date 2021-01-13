import csv


'''csv写入'''
# f = open('data.csv',mode='w',encoding='utf8',newline='')
# csvfile = csv.writer(f)
# csvfile.writerows([('token','title','tab','content'),('01','hellow','ask','xxxxxxxxxxx'),('02','hellow','ask','xxxxxxxxxxx')])

'''csv读取'''
f = open('test_data.csv',mode='r',encoding='utf8')
csvfile = csv.reader(f)
#去除第一行
title = next(csvfile)
test_data =[]
for line in csvfile:
    a = tuple(line)
    test_data.append(a)
print(title)
print(test_data)

'''写入数据'''
# from config.config_data import accesstoken
# f = open('test_data.csv',mode='w',encoding='utf8',newline='')
# csvfile = csv.writer(f)
# csvfile.writerow(['test_data','status_code','expected_error_msg'])
# csvfile.writerows([
#     ({'accesstoken':'','title':'hellords','tab':'ask','content':'cccccccccc'},401,'错误的accessToken'),
#     ({'accesstoken':accesstoken,'title':'','tab':'ask','content':'cccccccccc'},400,'标题不能为空'),
#     ({'accesstoken':accesstoken,'title':'sfdsdf','tab':'','content':'cccccccccc'},400,'必须选择一个版块'),
#     ({'accesstoken':accesstoken,'title':'asdfdsf','tab':'ask','content':''},400,'内容不可为空')
# ])