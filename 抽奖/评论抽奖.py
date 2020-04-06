import requests
import re
import time
import random
#Thank 小学妹@英俊的沈醉 for this script!!
lists={}
def get(page):
    global lists
    headers = {
        'Host': 'api.bilibili.com',
        'Referer': 'https://www.bilibili.com/video/av76848450',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
    }
    url = 'https://api.bilibili.com/x/v2/reply?callback=jQuery1720476389011894093_1574870017885&jsonp=jsonp&pn='+str(page)+'&type=1&oid=76848450&sort=2&_=1574870020413'
    request = requests.get(url, headers=headers).text
    select = '''\('''
    began = re.search(select, request).span()[1]
    request = request[began:-1]
    true = "true"
    false = "false"
    null = "null"
    req = eval(request)
    data = req["data"]
    # print(data)
    replies = data['replies']
    for i in replies:
        uid = i['member']['mid']
        name = i['member']['uname']
        lists[uid] = name
if __name__=="__main__":
    page=int(input("从前几页评论中抽取:"))
    for i in range(page):
        print("正在获取第%d页数据..."%(i+1))
        get(i+1)
        time.sleep(0.5)
    print("前%d页中共有%d人参与评论"%(page,len(lists)))

    num=int(input("输入抽奖人数:"))
    user_list=list(lists.items())
    win_list=[]
    for i in range(num):
        rand=random.randint(0,len(user_list)-1)
        win_list.append(user_list[rand])
        del user_list[rand]
    for i in range(num):
        print("第%d位中奖用户    用户名:%s    UID:%s"%(i+1,win_list[i][1],win_list[i][0]))