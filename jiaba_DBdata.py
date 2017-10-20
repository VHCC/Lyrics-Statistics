# -*- coding: utf-8 -*-
import MySQLdb
import jieba

file_origin = '/Users/user/Desktop/songs.txt'
file_count = '/Users/user/Desktop/statistics.txt'

db = MySQLdb.connect('localhost', 'root', 'F0973138343f', 'lyrics', charset='utf8')
cursor = db.cursor()

# execute SQL
cursor.execute("SELECT title, content FROM lyricsdb;")

# fetch result
# results = cursor.fetchall()

# print
# for record in results:
#   col1 = record[0]
#   print "%s" % (col1)

# all count in db precisely
rc = cursor.rowcount

word_list = []  # 分词列表
word_dict = {}  # 分词词频字典
word_frequency_array = []  # 分词词频列表
filterList = [
    ':',
    '[',
    ']',
]

count = 0

with open(file_origin, 'a') as f1, open(file_count, 'w') as f2:
    f1.truncate()
    f2.truncate()
    # take one data one time
    for i in range(0, rc):
        record = cursor.fetchone()
        title = record[0]
        col1 = record[1]
        f1.write(title.encode('utf-8') + ", " + col1.encode('utf-8') + "\n")
        words = jieba.cut(col1, cut_all=True)
        print i ,':' ,"%s" % (col1)

        value_cut = jieba.cut_for_search(col1)

        for cut in value_cut:
            word_list.append(cut)
        count += 1
        # print("共处理" + str(count) + "条数据,进行了中文分词！")
        # 统计词频
        for word in word_list:
            if not word.strip():
                continue
            if word in filterList:
                continue
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1

    # 保存数据到文件
    for key in word_dict:
        # 保存词频到列表
        # f2.write(key.encode('utf-8') + ' ' + str(word_dict[key]) + "\n")
        item = (key, word_dict[key])
        word_frequency_array.append(item)
    for frequency in sorted(word_frequency_array, key=lambda word: word[1], reverse=True):
        f2.write(frequency[0].encode('utf-8') + ' ' + str(frequency[1]) + "\n")

# close connection
db.close()