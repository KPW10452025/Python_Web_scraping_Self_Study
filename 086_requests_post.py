# 百度翻譯
# https://fanyi.baidu.com
# 翻譯詞彙 eye

import requests

url = 'https://fanyi.baidu.com/sug'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

data = {
    'kw' : 'eye'
}

# 實現 requests 的 post 請求
# url 請求地址
# data 請求參數
# kwargs 請求字典
response = requests.post(url=url, data=data, headers=headers)

content = response.text

# print(content)
# {"errno":0,"data":[{"k":"eye","v":"n. \u773c\u775b; \u89c6\u529b; \u773c\u72b6\u7269; \u98ce\u7eaa\u6263\u6263\u773c vt. \u5b9a\u775b\u5730\u770b; \u6ce8\u89c6; \u5ba1\u89c6; \u7ec6\u770b"},{"k":"Eye","v":"[\u4eba\u540d] \u827e; [\u5730\u540d] [\u82f1\u56fd] \u827e\u4f0a"},{"k":"EYE","v":"abbr. European Year of the Environment \u6b27\u6d32\u73af\u5883\u5e74; Iwas"},{"k":"eyed","v":"adj. \u6709\u773c\u7684"},{"k":"eyer","v":"n. \u6ce8\u89c6\u7684\u4eba"}]}

import json

obj = json.loads(content)

print(obj)
# {'errno': 0, 'data': [{'k': 'eye', 'v': 'n. 眼睛; 视力; 眼状物; 风纪扣扣眼 vt. 定睛地看; 注视; 审视; 细看'}, {'k': 'Eye', 'v': '[人名] 艾; [地名] [英国] 艾伊'}, {'k': 'EYE', 'v': 'abbr. European Year of the Environment 欧洲环境年; Iwas'}, {'k': 'eyed', 'v': 'adj. 有眼的'}, {'k': 'eyer', 'v': 'n. 注视的人'}]}

# 小結論
# (1)post 請求不需要編解碼
# (2)post 請求的參數是 data
# (3)不需要請求物件訂製 
