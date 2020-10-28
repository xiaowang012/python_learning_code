#coding=utf-8
import requests
import json
from jsonpath import jsonpath
import pprint as pd
import pandas
import time
import random

def get_content(url):
    response = requests.get(url)
    data = json.loads(response.text)
    created_at = jsonpath(data, '$..mblog.created_at')  # 发布日期
    reposts_count = jsonpath(data, '$..mblog.reposts_count')  # 转发
    comments_count = jsonpath(data, '$..mblog.comments_count')  # 评论
    attitudes_count = jsonpath(data, '$..mblog.attitudes_count')  # 赞
    # obj_ext = jsonpath(data, '$..mblog.obj_ext')    #有视频就有观看数据，无视频则无此字段
    raw_text = jsonpath(data, '$..mblog.raw_text')  # 发布内容
    data_list = []
    for i in range(len(created_at)):
        temp = {}
        temp['created_at'] = created_at[i]
        temp['reposts_count'] = reposts_count[i]
        temp['comments_count'] = comments_count[i]
        temp['attitudes_count'] = attitudes_count[i]
        temp['raw_text'] = raw_text[i]
        data_list.append(temp)
    return data_list

# def run():
#     df_sum = pd.DataFrame(columns=['created_at', 'reposts_count', 'comments_count', 'attitudes_count', 'raw_text'])
#     for i in range(1, 10):
#         time.sleep(random.random() * 3)
#         url = 'https://m.weibo.cn/api/container/getIndex?uid=6209296959&t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E5%89%91%E4%B8%89%E8%93%9D%E5%9B%BE-%E6%B8%85%E5%A2%A8%E5%9D%8A&type=uid&\
#         value=6209296959&containerid=1076036209296959&page={}'.format(i)
#         # if url == None:
#         #     break
#         data_list = get_content(url)
#         df = pd.DataFrame(data_list)
#         df_sum = pd.concat([df_sum, df], ignore_index=True)
#         print(df)
#     df_sum.to_csv('./data000.csv', encoding='utf-8-sig')


# if __name__ == '__main__':
    # run()

print(get_content('https://s.weibo.com/weibo?q=武汉&wvr=6&b=1&Refer=SWeibo_box'))