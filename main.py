# -*- coding = utf-8 -*-
import requests
import json
#获取access token
ID = ""
agentid =  #需要为整形
corpsecret = ""
ac = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s"%(ID,corpsecret))
dict = json.loads(ac.text)
access_token = dict["access_token"]
#推送消息
pushurl = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s&debug=1"%access_token
json = {
    "touser":"@all",
    "msgtype":"textcard",
    "agentid":agentid,
    "textcard":{
        "title":"测试通知",
        "description":"测试",
        "url":"http://127.0.0.1" #如有需要，自行替换
    },
    "safe":"1"
}

push = requests.post(pushurl,json=json)
print(push.text)