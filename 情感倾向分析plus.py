import aip
import time
import pandas as pd
from tqdm import tqdm

content_list=[]
positive_prob_list=[]
negative_prob_list=[]




def sentiment_classify(txt):
    client_appid = '55943552'
    client_ak = 'HiAemsnhDayUDVjSgGwmpqSP'
    client_sk = 'OYyfMziRSihJhUus7lMIQ9QthdfxTA7g'
    my_nlp = aip.nlp.AipNlp(client_appid, client_ak, client_sk)


    results=my_nlp.sentimentClassify(txt)
    positive_prob=results['items'][0]['positive_prob']
    negative_prob=results['items'][0]['negative_prob']


    content_list.append(txt)
    positive_prob_list.append(positive_prob)
    negative_prob_list.append(negative_prob)

    return positive_prob


df = pd.read_excel("C:/Users/29550/OneDrive/Desktop/评论中评.xlsx")

txt_content = df['评论内容']
# print(txt_content)


positive_times=0
negative_times=0
for txt in tqdm(txt_content):
    time.sleep(2)
    if sentiment_classify(txt)>0.5:
        positive_times+=1
    else:
        negative_times+=1


df_res = pd.DataFrame({"content":content_list, "positive_prob":positive_prob_list,"egative_prob":negative_prob_list})
df_res.to_excel('C:/Users/29550/OneDrive/Desktop/评论中评情感分析结果.xlsx')

print('分析完成，正向{}条，负向{}条'.format(positive_times,negative_times))



