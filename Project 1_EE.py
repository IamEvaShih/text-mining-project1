
# coding: utf-8

import json

theses = json.load(open('nthu_thesis20170330.json'))

theses[0].index('系所名稱')

theses[0].index('中文關鍵詞')


##把系所 與 英文關鍵字 個別抓出
data_list = [(thesis[2], thesis[17].split()) for thesis in theses[1:]]


data_list

index = []

#先列出所有的系所
i=0
while i < 5444:
    if data_list[i][0] not in index:
        index.append(data_list[i][0])
    i+=1
    
index

##這裡以電機工程學系為例，其他45個系所也是同樣照此步驟
##把list中 屬於電機工程學系的關鍵字，都加入ee這個list中
ee = []
j=0
while j < len(data_list):
    if data_list[j][0] == index[0]:
        ee.append(data_list[j][1])
    j+=1

ee


##去除list中的list 完全轉換為一個單一list
flat_ee = []
for sublist in ee:
    for val in sublist:
        flat_ee.append(val.lower())
flat_ee


#開始計算字的數量
from collections import Counter
counter_ee = Counter(flat_ee)
counter_ee


#把它從次數高到低
sort_ee = sorted(counter_ee.items(), key=lambda x: -x[1])
sort_ee


##要把它轉換為 wordcloud網站的格式 前面次數 後面是字
m=0
while m < len(sort_ee):
    print (sort_ee[m][1], sort_ee[m][0])
    m=m+1

    
##再把上面結果複製到：
## https://timdream.org/wordcloud2.js/#les-miz  產生word cloud
##各系所的word cloud共46個，存放在一同繳交的pdf當中，包含priject的細項說明。

