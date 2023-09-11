import requests


def get_location(domain):
    url = f"http://ip-api.com/json/{domain}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        latitude = data["lat"]
        longitude = data["lon"]
        return latitude, longitude
    else:
        return None


# 示例使用
domain = "www.baidu.com"
location = get_location(domain)

if location:
    latitude, longitude = location
    print(f"域名 {domain} 的位置经纬度为：{latitude}, {longitude}")
else:
    print(f"无法获取域名 {domain} 的位置信息")