#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import requests, json, sys
import urllib


def Get_Apps(query, cookie):
    headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.9(0x1800092e) NetType/WIFI Language/zh_CN"}
    url = "https://mp.weixin.qq.com/wxa-cgi/innersearch/mmbizwxasearchapp"
    # params = "query=" + query + "&cookie=" + cookie + '&subsys_type=1&offset_buf={"page_param":[{"subsys_type":1,"server_offset":0,"server_limit":' + str(int(number)+30) + ',"index_step":' + number + ',"index_offset":0}],"client_offset":0,"client_limit":' + number + '}'
    params = "query=" + query + "&cookie=" + cookie
    response = requests.post(url=url, params=params, headers=headers).text
    Apps_Json = json.loads(response)
    App_Items = Apps_Json.get('resp').get('json')
    App_Items = json.loads(App_Items)
    App_Items = App_Items.get('data')


    for App_Item in App_Items:

        App_Item_Json = App_Item.get('items')  # 重新加载嵌套内容中的json数据
        for i in App_Item_Json:
            App_Id = i.get('appid')
            #print App_Id
            App_Name = i.get('nickName')
            #App_Name = App_Item.get('nickName')
            App_Id_List.append(App_Id)
            App_Name_List.append(App_Name)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')  # 解决编码问题
    query = raw_input("请输入要搜的微信小程序名称: ")
    # query = query.decode('gbk', 'replace')
    # query = urllib.quote(query.encode('utf-8', 'replace'))
    query = urllib.quote(query.encode('utf-8'))
    # number = raw_input("请指定要返回的小程序的数量: ")
    cookie = raw_input("请输入你获取到的Cookie信息: ")
    # cookie = "aPtmmX%252BzOLBvWdkWE8R%252FloVZsru05Sd%252BhXbvgEaKkTMmo5LEb0jX1UUB0uoc1usMeIDB2xkWitp4%252FpTtNCbuKA%253D%253D%257C%257C%257Cdc885065190336fa5b5d5d59f7c91591e3fc4c92ae9a7d2d881565599c066ca7e3fffc2fe569c83bd36756bf5fe3609a5b63fbeead94432cabbb335589f2d7895ec71c84dc64255efd032ea77d98fdf7e8a662c336d7f3e48f9a0ad6e0807fe8ffe5f15a81da642abbb1f77e82196a904998d3a2298e9eb170a0b3ec4b19c299"
    App_Id_List = []
    App_Name_List = []
    try:
        Get_Apps(query, cookie)
        for i in range(len(App_Name_List)):
            print(App_Id_List[i]),
            print(App_Name_List[i])
    except:
        print("信息获取失败，请检查！")
