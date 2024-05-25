import jieba
import wordcloud

# 读取文本
with open("C:/Users/29550/OneDrive/Desktop/郁美净差评.txt", encoding="gb18030") as f:
    s = f.read()
# print(s)
# 生成分词列表
list_s = jieba.lcut(s)
# print(ls)
# 用空格连接成字符串文本
text = ' '.join(list_s)
# print(text)
# 将不需要显示的词整理好后，放入stopwords中
stopwords = ["宝宝","孩子","知道","京东","给","是", "的", "了", "很","也", "用", "还是", "好", "买", "感觉","没有","我","非常","不","吧","都","有点","hellip","就","这个","还","说"]
# 创建词云对象
wc = wordcloud.WordCloud(font_path="msyh.ttc",
                         width=2000,
                         height=1125,
                         background_color='white',
                         max_words=100,
                         stopwords= stopwords )
# msyh.ttc是电脑本地字体，也可以写成绝对路径，字体也可以根据需求换其他字体文件
wc.generate(text)  # 加载词云文本
wc.to_file("C:/Users/29550/OneDrive/Desktop/郁美净差评.png")  # 保存词云图文件