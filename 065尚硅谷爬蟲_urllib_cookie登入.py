# 適用場景，在數據採集的時候需要繞過登入。

# 常見反爬蟲手段之一
# 需登入後才有訪問權的頁面雖然是 utf-8 編碼，但是登入頁面卻不是 utf-8

import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://10fastfingers.com/settings/'

headers = {
    # cookie 中攜帶著個人登入訊息，如果有登入之後 cookie，那我們就可以帶著 cookid 進入各個頁面
    'cookie': "_ga=GA1.2.431756726.1631446672; CookieConsent={stamp:%27NztDfW70IeZxu7yUqP7R4XE7RjkhGaLmNC2NhrGHNjfwY0DqA6bDSQ==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:2%2Cutc:1631446694208%2Cregion:%27tw%27}; _gid=GA1.2.1379434827.1631618440; _fssid=d24897c7-a606-4b9e-8daf-9e58e92eaf1b; _pbjs_userid_consent_data=3524755945110770; _pubcid=963b7b8a-8b77-4377-ae61-6027c3a678e4; __qca=P0-613908928-1631816434116; _cc_id=f855e32731ab87075862931855c1220d; _lr_env_src_ats=false; phpbb3_7228a_u=1; phpbb3_7228a_k=; phpbb3_7228a_sid=badcb3423f2c05670d199ff33711a706; CakeCookie[lang]=Q2FrZQ%3D%3D.5exP; fsbotchecked=true; __gads=ID=42372d92160be895:T=1631816437:S=ALNI_MZ3qEMIx253nxBCMpzHpdDWrQJLng; pbjs-unifiedid=%7B%22TDID%22%3A%2239e9d67d-6141-49ab-9c68-a4bcc7b3dd5f%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222021-09-09T08%3A17%3A25%22%7D; pbjs-unifiedid_last=Sat%2C%2009%20Oct%202021%2008%3A17%3A25%20GMT; panoramaId_expiry=1634889594266; panoramaId=f4e3aae90918fcb71586af21fb9116d53938c2c9702dd8d8c312a2e9a8707b7b; cookie=%7B%22id%22%3A%2201FFQXDQ4ZPG00YD0R7E339YPP%22%2C%22ts%22%3A1634625400267%7D; _lr_retry_request=true; CakeCookie[alternate_language_suggestion]=Q2FrZQ%3D%3D.9PBdWA%3D%3D; CAKEPHP=l4t9q2650fimvrofd75d3gfj6v; CakeCookie[remember_me_cookie]=Q2FrZQ%3D%3D.4bUQXmA06xPhjpJArwVn7qMvJL%2B3PLwOg%2B9Cg%2BKAdEct8%2Fl%2FlHzqZA%3D%3D; _gat=1; cto_bidid=Rp5THl9oJTJCY1NTaDZ4b00wemdXcnMyZkUwZGclMkJDNWpJVWpOR2VJSGdGZmRrR0tZa1o3bkQxTk9FeVpCc1ZDODVTQnFSREpuWGlZSDZCak55SmJUUGRKUUh2WHhvM05aJTJGUElWYWRQR292cHVjSUJpJTJCakRwY0hIc2piOENaN2g4eWg2ckx1MiUyQkVjdHFTa3ZBRDR2ZHlGMGhjbmtBJTNEJTNE; cto_bundle=GECZXl9qMmMwUVlEVVBJYXZEZk9zUDhPbFlHSzFsdyUyQmYlMkZ0aHRaUXhsUTlmazBnVnI5eUpLcDNXUERZdjNhWjNZZE5VcEwxRW5vRVNrT1VlNXdhYWhRMXo1UFhHbWNSUXlTSlhBQVlKdHI4SktpZHRGMiUyRmFZSnYwaCUyQmdxcjlxY1QzNllWSmRmJTJGUSUyRkpwMnVwU3hObWhUc0FzMDdnelZCYVVEJTJCViUyQm9UUkJoJTJGOGtaNlQ2eTg0dWdNdnFqQ29FOEVzeVN5dkRhRVFCMnUlMkIyakd5dDdyUk5NQ0plN0ElM0QlM0Q; cto_bundle=JvehlF9qMmMwUVlEVVBJYXZEZk9zUDhPbFlINWUlMkZQVDhQS2M1Zk9EekJvMUZwQWdvclc2c0w0QSUyRk1LbmdQeUFJSGZMOFAyMEJURlpSS3QybFppUmJMRklFcmtpeGc3WjlvVjFNYzFXWkk0bXNLcDVOdDFkJTJCdzNhTkRkZkFnc1NmM0tVbEVVZXRsUkhRRVVhVnZOdk9hcWJNY0w4WnFsMHg2OUh3THJ3S3NVb0R3MCUyRmVNRmJiaGg4cjdUUlp2VzZ4YWpIUzNZYVp0JTJCYmR5ajhkRGFiN1RxdElsQSUzRCUzRA",
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    # referer：判斷當前物鏡是不是由 referer 表示的路徑而來，很多網站會把 referer 當作圖片防盜鏈
    'referer': 'https://10fastfingers.com/typing-test/english',
}

request = urllib.request.Request(url = url, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)

with open("typing_web.html", mode = "w", encoding="utf-8") as fp:
    fp.write(content)

# 小結論
# 通常 headers 中弄好 user-agent, cookie, referer 就能搞定八成左右的網站
