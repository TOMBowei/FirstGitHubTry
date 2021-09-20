import csv    #加载csv包便于读取csv文件
import wordcloud
import matplotlib.pyplot as plt
import numpy as np


csv_file=open('/Users/wubowei/Documents/毕业设计源代码/friend.csv')    #打开csv文件
csv_reader_lines = csv.reader(csv_file)   #逐行读取csv文件
data=[]    #创建列表准备接收csv各行数据
hangshu = 0
for one_line in csv_reader_lines:
    data.append(one_line)    #将读取的csv分行数据按行存入列表‘date’中
    hangshu = hangshu + 1    #统计行数（这里是学生人数）
i=0
while i < hangshu:
    # print (date)    #访问列表date中的数据验证读取成功（这里是打印所有学生的姓名）
    i = i+1

for item in data:
    with open('friend.txt','a+') as f:
        f.write(str(item)+ '\n\n')
        f.close

# for item in date:
#     print(item[1])

# w = wordcloud.WordCloud
# w.generate(date)
# w.to_file(test.png)