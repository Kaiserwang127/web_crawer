import time
import requests
import json


#可视化函数
def process_bar(percent):
    repeat_times = int(percent*10)
    bar ='感情正向-->'+ '#'*repeat_times+'*'*(10-repeat_times)+'<--感情负向'
    print(bar)


host="https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=HiAemsnhDayUDVjSgGwmpqSP&client_secret=OYyfMziRSihJhUus7lMIQ9QthdfxTA7g"
response = requests.get(host)

mytoken = response.json()['access_token']


def txt_mark(mystr ,mytoken):
    content_txt = json.dumps({
        "text": mystr
    })
    headers = {
        'Content-Type': 'application/json',
    }


    url1 = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify"
    url = url1 + '?charset=UTF-8&access_token=' + mytoken
    results = requests.post(url=url, headers=headers, data=content_txt).json()
    #print(results)

    input_text=results['text']
    positive_prob= results['items'][0]['positive_prob']
    print(input_text)
    #print(positive_prob)


    process_bar(positive_prob)
    print('-'*40)


txt_mark("你好啊，很高兴见到你",mytoken)






