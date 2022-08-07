import requests
import re
from email.mime.multipart import MIMEMultipart
import smtplib
import datetime
from email.mime.text import MIMEText
import time
uid=input("请输入账号:")
upw=input("请输入密码:")
msg1=input("请输入发信人邮箱:")
passwd1=input("请输入发信人邮箱认证码:")
place=input("请输入打卡地点：（郑大北校区）")
isschool=input("请输入在校情况：")
dingweididan=input("请输入定位地点:")
emailto=input("请输入收信人邮箱：")
def email(z,e):
    now = datetime.datetime.now()
    msg = MIMEMultipart()
    msg_from =msg1
    passwd = passwd1
    msg_to = z+ "@qq.com"
    subject = "return heath"
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    content = "QAQ %s\n" % now+str(e)
    part = MIMEText(content)
    msg.attach(part)
    c=0
    while c != 1:
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, msg.as_string())
            s.quit()
            c = 1
        except:
            print("return false")

def email2(z):
    now = datetime.datetime.now()
    msg = MIMEMultipart()
    msg_from = msg1
    passwd = passwd1
    msg_to = z + "@qq.com"
    subject = "return heath"
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    content = "good morning >_< %s\n" % now
    part = MIMEText(content)
    msg.attach(part)
    c = 0
    while c != 1:
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, msg.as_string())
            s.quit()
            c = 1
        except:
            print("return false")
def returnhelth():
    url = "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login"
    header1 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'jksb.v.zzu.edu.cn',
        'Referer': 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36 SLBrowser/6.0.1.9171',
    }

    headers = {
        'Host': r'jksb.v.zzu.edu.cn',
        'Connection': r'keep-alive',
        'Content-Length': r'135',
        'Cache-Control': r'max-age=0',
        'sec-ch-ua': r'Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99',
        'sec-ch-ua-mobile': r'?0',
        'Upgrade-Insecure-Requests': r'1',
        'Origin': r'https://jksb.v.zzu.edu.cn',
        'Content-Type': r'application/x-www-form-urlencoded',
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Accept': r'textml,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': r'same-origin',
        'Sec-Fetch-Mode': r'navigate',
        'Sec-Fetch-User': r'?1',
        'Sec-Fetch-Dest': r'document',
        'Referer': r'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0',
        'Accept-Encoding': r'gzip, deflate, br',
        'Accept-Language': r'zh-CN,zh;q=0.9',
    }
    data = {
        'uid': uid,
        'upw': upw,
        'smbtn': r'%E8%BF%9B%E5%85%A5%E5%81%A5%E5%BA%B7%E7%8A%B6%E5%86%B5%E4%B8%8A%E6%8A%A5%E5%B9%B3%E5%8F%B0',
        "h28": "947"
    }


    response = requests.post(url=url, data=data, headers=headers)
    # print(response.text)
    p1 = re.compile(r'parent.window.location="https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first6\?(.*)"}}', re.S)
    urls = re.findall(p1, response.text)[0]
    pa=re.compile(r'ptopid=(.*?)&',re.S)
    pb=re.compile(r'&sid=(.*)',re.S)
    ptopid=re.findall(pa,urls)[0]
    sid=re.findall(pb,urls)[0]
    data1={
        "ptopid":ptopid,
        "sid":sid,
        "myvs_1":"否",
        "myvs_2":"否",
        "myvs_3":"否",
        "myvs_4":"否",
        "myvs_5":"否",
        "myvs_6":"否",
        "myvs_7":"否",
        "myvs_8":"否",
        "myvs_9":"y",
        "myvs_10":"否",
        "myvs_11":"否",
        "myvs_12":"否",
        "myvs_13a":"41",
        "myvs_13b":"4114",
        "myvs_13c":place,
        "myvs_14":"否",
        "myvs_14b":"",
        "myvs_30":isschool,
        "myvs_15": "否",
        "did":"2",
        "door":'',
        "day6":"b",
        "men6":"a",
        "myvs_13":"g",
        "myvs_24":"否",
        "myvs_26":"2",
        "memo22":dingweididan
    }
    data3={
        "day6":"b",
        "did":"1",
        "door":"",
        "men6":"a",
        "ptopid":ptopid,
        "sid":sid,
    }
    header2={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'jksb.v.zzu.edu.cn',
    'Referer': 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36 SLBrowser/6.0.1.9171',
    }
    url2="https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb?"+urls+"&fun2="
    response2=requests.post(url=url2,data=data3,headers=header2)
    url3 = "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb"
    response3 = requests.post(url=url3, headers=header2,data=data1)
    with open("aa.html",'wb') as fp:
        fp.write(response3.content)
    print("#"*6)
    print("finish")
    print("#"*6)
if __name__ == '__main__':
    time1 = "00:03:00.0000"
    time2 = "01:13:00.0000"
    print("server begin")
    email(emailto,"begin")
    while True:
        while True:
            now = str(datetime.datetime.now())
            now2 = now[11:]
            if time1 < now2<time2:
                try:
                    print("hello")
                    returnhelth()
                    email2(emailto)
                    break
                except Exception as e:
                    email(emailto,e)
            time.sleep(300)
        time.sleep(3600)


