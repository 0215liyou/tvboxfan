import requests
import json

try:
    # 获取原始内容
    url = "https://wekh.eu.org/tvbox/fan.json"
    response = requests.get(url)
    
    # 检查响应状态码
    if response.status_code != 200:
        print("Failed to fetch data from the server. Status code:", response.status_code)
        exit()

    original_content = response.text

    # 移除以 // 开头的注释
    lines = original_content.split('\n')
    cleaned_content = '\n'.join([line for line in lines if not line.strip().startswith('//')])

    # 尝试解析为 JSON 格式
    try:
        data = json.loads(cleaned_content)
    except json.JSONDecodeError as e:
        print("Failed to parse JSON data:", e)
        exit()

    # 修改内容
    data["lives"] = [
        {
            "name": "IPV6",
            "type": 0,
            "url": "https://wekh.eu.org/tvbox/iptv.txt",
            "playerType": 1,
            "ua": "okhttp/3.15"
        }
    ]

    # 将修改后的内容转换为 JSON 字符串，并指定 ensure_ascii=False 以确保汉字和表情符号正常显示
    modified_content = json.dumps(data, indent=2, ensure_ascii=False)

    # 将修改后的内容保存到文件tvbox.txt中，并指定编码格式为 UTF-8
    with open("tvbox.txt", "w", encoding='utf-8') as file:
        file.write(modified_content)

    print("内容已保存到tvbox.txt文件中")

except requests.RequestException as e:
    print("An error occurred during the request:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
