import json
import os


# 開檔
file_path = 'json.txt'
if os.path.isfile(file_path):
  f = open(file_path, 'r')
  json_str = f.read()
  # 轉json_str為dict
  json_obj = json.loads(json_str)
  # 輸入想搜尋的key
  user_input = input("請輸入想搜尋的key：")
  print("\n將為您輸出所有value：")

  # 遞迴搜尋
  def search_key(json_obj, user_input):
    # 最外層會先遇到字典吧，先寫字典的判斷
    if isinstance(json_obj, dict):
      for k, v in json_obj.items():
        if k == user_input:
          print(v)
        elif isinstance(v, (dict, list)):
          # 這是說如果解析，key不是我們要搜尋的，就繼續查找，看型態是物件還是陣列
          search_key(v, user_input)
    elif isinstance(json_obj, list):  # 如果解析到陣列就分析陣列每個元素
      for node in json_obj:
        search_key(node, user_input)

  # 輸出結果
  search_key(json_obj, user_input)
  f.close()
