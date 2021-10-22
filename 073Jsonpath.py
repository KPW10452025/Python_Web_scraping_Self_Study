import jsonpath
import json

obj = json.load(open('073Jsonpath.json', 'r', encoding = 'utf-8'))

# print(obj)
# {'store': {'book': [{'category': '修真', 'author': '六道', 'title': '壞蛋怎麼煉成的', 'price': 8.95}, {'category': '修真', 'author': '天讒土豆', 'title': '抖破蒼穹', 'price': 12.99}, {'category': '修真', 'author': '唐家三少', 'title': '斗羅大陸', 'isbn': '0-553-21311-3', 'price': 8.99}, {'category': '修真', 'author': '南派三叔', 'title': '星辰變', 'isbn': '0-395-19395-8', 'price': 22.99}], 'bicycle': {'color': '黑色', 'price': 19.95}}}

author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
print(author_list)
# ['六道', '天讒土豆', '唐家三少', '南派三叔']

the_data = jsonpath.jsonpath(obj, '$.store.book[1].author')
print(the_data)
# ['天讒土豆']

the_data = jsonpath.jsonpath(obj, '$..author')
print(the_data)
# ['六道', '天讒土豆', '唐家三少', '南派三叔', '無極天尊']

the_data = jsonpath.jsonpath(obj, '$.store.*')
print(the_data)
# [[{'category': '修真', 'author': '六道', 'title': '壞蛋怎麼煉成的', 'price': 8.95}, {'category': '修真', 'author': '天讒土豆', 'title': '抖破蒼穹', 'price': 12.99}, {'category': '修真', 'author': '唐家三少', 'title': '斗羅大陸', 'isbn': '0-553-21311-3', 'price': 8.99}, {'category': '修真', 'author': '南派三叔', 'title': '星辰變', 'isbn': '0-395-19395-8', 'price': 22.99}], {'author': '無極天尊', 'color': '黑色', 'price': 19.95}]

the_data = jsonpath.jsonpath(obj, '$.store..price')
print(the_data)
# [8.95, 12.99, 8.99, 22.99, 19.95]

the_3re_book = jsonpath.jsonpath(obj, '$..book[2]')
print(the_3re_book)
# [{'category': '修真', 'author': '唐家三少', 'title': '斗羅大陸', 'isbn': '0-553-21311-3', 'price': 8.99}]

the_last_book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
print(the_last_book)
# [{'category': '修真', 'author': '南派三叔', 'title': '星辰變', 'isbn': '0-395-19395-8', 'price': 22.99}]
