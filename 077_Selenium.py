import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.jd.com/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

print(content)
