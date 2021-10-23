import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1634959435578_152&jsoncallback=jsonp153&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1634959435578_152&jsoncallback=jsonp153&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 't=2c80ab18e29b741f3e564df7b0af3717; cookie2=1111971973f65816fed7b5b3b1a5abbb; v=0; _tb_token_=7a0b873ebe78e; cna=eOfEGVx5xQwCAdyOS2Vflc60; xlly_s=1; tb_city=110100; tb_cityName="sbG+qQ=="; tfstk=csA1BPv9gndeNQM4_FgU0HFgVg5VCPN18VsH5KtMYlWKw0EPvS10h7SWeoL0vs7AR; l=eBIpBPreg1p7QrsfBO5aPurza77O3IRb4-VzaNbMiInca1udtF15UNCLoEAySdtj_tCvsetr0HqPDRLHRnOgCc0c07kqm07t3xvO.; isg=BPz8CbcasfxSwoUhUjNiJmgdzZyu9aAffVThbNZ9l-fKoZwr_gTNr0gfgcHZ09h3',
    'referer': 'https://dianying.taobao.com/?spm=a1z21.3046609.city.1.32c0112akgErOM&city=110100',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
