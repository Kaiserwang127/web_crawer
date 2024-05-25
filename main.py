
import requests
import json


class Jdcomment_spider(object):

    def __init__(self,file_name='jingdong_pinlun'):
        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
        }

        #打开文件
        self.fp=open('./jingdong_pinlun.txt','w',encoding='utf-8')


        print(f'爬虫开始打开{file_name}文件！')

    def parse_one_page(self,url):
       # url = 'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1708961609762&loginType=3&uuid=181111935.1706882521848703693657.1706882521.1706882522.1708961141.2&productId=2882974&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1&bbtf=&shield='

        response = requests.get(url, headers=self.headers)

        """
        print(response)

        print(response.text)

        print(type(response.text))

        print(response.request.headers)

        """

        js_data = json.loads(response.text)
        """
        print(js_data)
        print(type(js_data))
        """
        # js_data就是字典形式

        comment_list = js_data['comments']

        for comment in comment_list:
            goods_id = comment.get('id')
            nickname = comment.get('nickname')
            score = comment.get('score')
            productSize = comment.get('productSize')
            creationTime = comment.get('creationTime')

            content = comment.get('content')
            content = ''.join(content.split('\n'))  # 处理换行符号


            print(content)


            #存储数据
            self.fp.write(f'{goods_id}\t{nickname}\t{score}\t{productSize}\t{creationTime}\t{content}\n')

    def parse_max_page(self):
        for page_num in range(23):
            print(f'正在抓取第{page_num}页的数据！')
            #郁美净瓶装https://item.jd.com/100000597560.html#none
            #好评 url = f'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1708961609762&loginType=3&uuid=181111935.1706882521848703693657.1706882521.1706882522.1708961141.2&productId=2882974&score=0&sortType=5&page={page_num}&pageSize=10&isShadowSku=0&fold=1&bbtf=&shield='
            #差评url = f'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1709017323305&loginType=3&uuid=181111935.1706882521848703693657.1706882521.1706882522.1708961141.2&productId=2882974&score=1&sortType=5&page={page_num}&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield='
            #中评url=f'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1709020263284&loginType=3&uuid=181111935.1706882521848703693657.1706882521.1706882522.1708961141.2&productId=2882974&score=2&sortType=5&page={page_num}&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield='

            #青蛙王子瓶装https://item.jd.com/7213796.html#none
            #好评url=f'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1709736115882&loginType=3&uuid=181111935.1706882521848703693657.1706882521.1708961141.1709733876.3&productId=7213796&score=3&sortType=5&page={page_num}&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield='
            #中评url=f'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1709737756010&loginType=3&uuid=181111935.1706882521848703693657.1706882521.1708961141.1709733876.3&productId=7213796&score=2&sortType=5&page={page_num}&pageSize=10&isShadowSku=0&fold=1&bbtf=&shield='
            url=f'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1709738707734&loginType=3&uuid=181111935.1706882521848703693657.1706882521.1708961141.1709733876.3&productId=7213796&score=1&sortType=5&page={page_num}&pageSize=10&isShadowSku=0&fold=1&bbtf=&shield='
            self.parse_one_page(url=url)



    def close_files(self):
        self.fp.close()
        print('爬取完毕，关闭文件！')







if __name__=='__main__':
    #实例化一个对象
    jd_spider=Jdcomment_spider()
    #调用方法
    jd_spider.parse_max_page()
    #关闭文件
    jd_spider.close_files()