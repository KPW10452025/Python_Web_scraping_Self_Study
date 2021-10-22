import jsonpath
import json

obj = json.load(open('073Jsonpath.json', 'r', encoding = 'utf-8'))

print(obj)
# {'store': {'book': [{'category': '修真', 'author': '六道', 'title': '壞蛋怎麼煉成的', 'price': 8.95}, {'category': '修真', 'author': '天讒土豆', 'title': '抖破蒼穹', 'price': 12.99}, {'category': '修真', 'author': '唐家三少', 'title': '斗羅大陸', 'isbn': '0-553-21311-3', 'price': 8.99}, {'category': '修真', 'author': '南派三叔', 'title': '星辰變', 'isbn': '0-395-19395-8', 'price': 22.99}], 'bicycle': {'color': '黑色', 'price': 19.95}}}
