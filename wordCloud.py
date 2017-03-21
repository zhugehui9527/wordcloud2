# -*- coding:utf-8 -*-
from os import path
import jieba
from wordcloud import WordCloud,STOPWORDS
# from scipy.misc import imread
import matplotlib.pyplot as plt


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

stopwords = {}
# 定义过滤不显示的词库
def stopword(filename = ''):
    global stopwords
    with open( filename,'rb') as f :
        line = f.readline().rstrip()
        while line:
            stopwords.setdefault(line,0)
            stopwords[line.decode('utf-8')] = 1
            line = f.readline().rstrip()

        f.close()

#定义中文分词和停用词清洗

def cleancntxt(txt, stopwords):

    seg_generator = jieba.cut(txt, cut_all=False)

    seg_list = [i for i in seg_generator if i not in stopwords]

    seg_list = [i for i in seg_list if i != u' ']

    return(seg_list)


# 定义中文词云函数
def wordcloudplot(txt,cloudpic):
    # coloring = imread(imagename) # 读取背景图片
    wordcloud = WordCloud(max_font_size=150,# 字体最大值
                          font_path=font_path,# 兼容中文字体
                          stopwords=STOPWORDS,# 停止词
                          random_state=42,#随机状态
                          background_color="black",# 背景颜色
                          margin=10,# 最大显示
                          width= 500,# 宽度
                          height=300,# 高度
                          # mask=coloring,# 设置背景图片
                          max_words=2000 # 词云显示的最大词数
                          ).generate(txt)
    # 生成图片
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    # 绘制词云
    plt.figure()
    #保存图片
    wordcloud.to_file(cloudpic)

def plotTitleCloud(txtlist,cloudpic):

    txt = r' '.join(txtlist)

    seg_list = cleancntxt(txt, stopwords)

    #seg_list = jieba.cut(txt, cut_all=False)

    txt = r' '.join(seg_list)

    wordcloudplot(txt,cloudpic=cloudpic)

if __name__ == '__main__':
    d = path.dirname(__file__)

    font_path = path.join(d, 'msyh.ttf')# 中文字体路径
    stopfile = path.join(d, 'stopwords.txt') #不显示的词库
    filename = path.join(d, 'constitution.txt') #待分词的词库
    cloudpic = path.join(d, 'wordcloud.png') #保存词云图片路径
    imagename = path.join(d, "dragon.jpg")  # 背景图片路径
    stopword(stopfile)
    with open (filename) as f:
        t1 = f.readlines()
        plotTitleCloud(t1,cloudpic)
