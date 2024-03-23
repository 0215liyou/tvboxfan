import re
import base64
import requests

headers = {'User-Agent': 'okhttp/3.15'}

url = 'http://饭太硬.top/tv'
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 抛出异常，处理错误的响应状态

    # 使用正则表达式查找匹配项
    match = re.search(r'[A-Za-z0]{8}\*\*(.*)', response.text)
    
    if not match:
        print("在响应文本中未找到匹配项。")
    else:
        result = match.group(1)
        content = base64.b64decode(result).decode('utf-8')

        # 将解码后的内容写入到 fan.json 文件中
        with open('fan.json', 'w', newline='', encoding='utf-8') as f:
            f.write(content)

except requests.RequestException as e:
    print("请求失败:", e)
except Exception as ex:
    print("发生错误:", ex)
else:
    print("数据成功写入到 fan.json 文件中。")
