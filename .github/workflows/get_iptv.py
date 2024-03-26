import requests

# 获取直播源链接
url = "https://tv.wwkh.eu.org/txt/fmml_ipv6.txt"
response = requests.get(url)
playlist = response.text

# 将直播源链接保存到iptv.txt文件中
with open("iptv.txt", "w") as file:
    file.write(playlist)
