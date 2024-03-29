'''
文件描述：基于微信公众号实现AI客服
作者：zhangmeiling
邮箱：2570415385@qq.com
时间:2019-06-24
'''


#!/user/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse

def get_robot_reply(question):
    '''
    函数功能:对于特定问题进行特定回复，对于非特定问题进行智能回复

    参数描述：
    question 聊天内容或问题

    返回值：str,回复内容

    '''
    # print("问题：")
    # question = input()
    


    if "你叫什么名字" in question:
        answer = "我是小西瓜"
    elif "我还有多少钱" in question:
        answer = "100元"
    elif "你多少岁"in question:
        answer = "3"
    elif "你是小哥哥还是小姐姐" in question:
        answer = "你猜啊"
    else:
        try:
            # 调用NLP接口实现智能回复
        
            params = urllib.parse.urlencode({'msg':question}).encode()  #接口参数需要进行URL编码
            req = urllib.request.Request("http://api.itmojun.com/chat_robot",params,method="POST")
            answer = urllib.request.urlopen(req).read().decode() #调用接口(即向目标服务器发出HTTP请求，并获取服务器的响应)
        except Exception as e:
            answer = "AI机器人出现故障！（原因：%s）" % e


    return answer


if __name__ == '__main__':
    #测试get_robot_reply函数
    # print(get_robot_reply("你叫什么名字"))
    # print(get_robot_reply("你多少岁"))
    # print(get_robot_reply("石首今天天气如何"))
    # print(get_robot_reply("你是男是女"))
    # print(get_robot_reply("你到底是谁"))
    # print(get_robot_reply("question"))
    while True:
        question = input("\n我说：")
        answer = get_robot_reply(question)
        print("\n小魔仙说：%s" %answer)

